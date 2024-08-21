import cv2
from ultralytics import YOLO
import numpy as np
import serial 
import time 
from collections import deque 

# YOLO predict documentation: https://docs.ultralytics.com/modes/predict/#inference-arguments
'''
TODO: 
- Add stop button on manual mode. 
- Process exceptions. 
- #1. 조준모드에서 불 안보이면 보일때까지 가만히 있는 예외 
- 
'''

class Motor: 
    def __init__(self): 
        self.model = YOLO("../../data/best.pt") 

        self.py_serial = serial.Serial(
            port='/dev/ttyACM0', 
            # port='/dev/cu.usbmodem22201', 
            baudrate=9600, 
            timeout=1 
        )

        # Webcam settings 
        self.cap = cv2.VideoCapture(2) 
        # self.cap = cv2.VideoCapture(0) 
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 640 480 
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH) 
        self.offset_x = 120 
        self.offset_y = 90
        self.crosshair = 40

        # 상태 전환 설정 
        self.state = 0 
        status_frames = 10 
        self.isFireList = deque(maxlen=status_frames) 
        self.isFireCentered = deque(maxlen=status_frames) 

        # 데이터 수신 
        self.flameStatus = None 
        self.waterStatus = None 
    
    def __del__(self): 
        self.cap.release() 
        cv2.destroyAllWindows() 
    
    def get_pred(self): 
        ret, frame = self.cap.read() 
        if not ret: 
            return 

        results = self.model.predict(source=frame, imgsz=640, conf=0.7, verbose=False) 

        max_area = 0 
        max_box = None 
        # max_confidence = None 
        # max_class = None
        
        for r in results: 
            boxes = r.boxes.xyxy.cpu().numpy() 
            confidences = r.boxes.conf.cpu().numpy() 
            classes = r.boxes.cls.cpu().numpy() 
            for box, confidence, cls in zip(boxes, confidences, classes): 
                x1, y1, x2, y2 = map(int, box) 
                area = (x2 - x1) * (y2 - y1) 
                if area > max_area:
                    max_area = area 
                    max_box = box 
                    # max_confidence = confidence 
                    # max_class = cls 
        
        if max_box is not None: 
            x1, y1, x2, y2 = map(int, max_box) 

            # 바운딩 박스 내의 영역 추출
            roi = frame[y1:y2, x1:x2]

            # HSV 색상공간으로 변환
            hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

            # 불 색상 범위 설정 (더 좁은 붉은 계열)
            lower_bound = np.array([0, 60, 60])
            upper_bound = np.array([25, 255, 255])

            # 범위 내의 색상 필터링
            mask = cv2.inRange(hsv, lower_bound, upper_bound)

            if np.sum(mask) > 0:  # 최소한의 불색상이 존재할 경우 
                # 불 유무 정보 
                self.isFireList.append(True) 
                
                # 바운딩 박스 그리기
                # label = f'{self.model.names[int(max_class)]} {max_confidence:.2f}'
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2
                # coordinates = f'Center: X: {center_x}, Y: {center_y}'

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                # cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                # cv2.putText(frame, coordinates, (x1, y2 + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

                # 중앙에 빨간 점 그리기
                cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1) 

            # 프레임상 불이 검출이 되었지만 2차검증을 통과하지 못하였을 경우 
            else: 
                self.isFireList.append(False) 

                center_x = None 
                center_y = None 
        
        # 불이 없을 경우 
        else: 
            self.isFireList.append(False) 

            center_x = None 
            center_y = None 

        return center_x, center_y, ret, frame 
    
    def read_ino(self): 
        res = self.py_serial.read_until(b'\r\n') 

        # 아두이노 ON 신호 추가시키기 
        if len(res) > 0: 
            self.flameStatus = res[0] 
            self.waterStatus = res[1] 
    
    def send_cmd(self, center_x, center_y, manual_cmd=None): 
        ## State transition part 
        if (self.state == 0) and (len(self.isFireList) == 10) and (False not in self.isFireList): 
            self.state = 1 
        else: 
            pass  
        
        if (self.state == 1) and (len(self.isFireCentered) == 10) and (False not in self.isFireCentered): 
            self.state = 2 
        else: 
            pass 
        
        if (self.state == 2) and self.flameStatus: 
            self.state = 3 
        else: 
            pass  
        
        if (self.state == 3) and (True not in self.isFireList): 
            self.state = 0 
        else: 
            pass 
        
        if (self.state == 4): 
            pass 


        ## Command part 
        self.cmd_list = [] 
        
        # patrol mode 
        if self.state == 0: 
            ("Patrol mode entered ========") 
            self.cmd_list.append("00") 
        
        # aiming mode 
        if ((self.state == 1) or (self.state == 3)) and center_x:  # state가 1인데 center_x, y값이 없으면 1초 렉걸린다. 이부분 처리하셈 
            print("Aiming mode entered ============")
            # 대략적인 위치로 회전
            if center_x < (self.width//2 - self.offset_x): 
                self.cmd_list.append("11") 
                # print("======== MOVE LEFT  ========") 
            elif center_x > (self.width//2 + self.offset_x): 
                self.cmd_list.append("12") 
                # print("======== MOVE RIGHT ========") 
            
            if center_y < (self.height//2 - self.offset_y): 
                self.cmd_list.append("13") 
                # print("======== MOVE  UP   ========") 
            elif center_y > (self.height//2 + self.offset_y): 
                self.cmd_list.append("14") 
                # print("======== MOVE DOWN  ========") 

            # 자세한 위치로 회전 
            if (center_x >= (self.width//2 - self.offset_x)) and (center_x < self.width//2): 
                self.cmd_list.append("15") 
                # print("======== MOVE LEFT SLOWLY  ========") 
            elif (center_x <= (self.width//2 + self.offset_x)) and (center_x > self.width//2): 
                self.cmd_list.append("16") 
                # print("======== MOVE RIGHT SLOWLY ========") 
            
            if (center_y >= (self.height//2 - self.offset_y)) and (center_y < self.height//2): 
                self.cmd_list.append("17") 
                # print("======== MOVE UP SLOWLY    ========") 
            elif (center_y <= (self.height//2 + self.offset_y)) and (center_y > self.height//2): 
                self.cmd_list.append("18") 
                # print("======== MOVE DOWN SLOWLY  ========") 
            
            # 조준 완료 확인 
            if ((center_x > self.width//2 - self.crosshair) and (center_x < self.width//2 + self.crosshair)) and \
                    ((center_y > self.height//2 - self.crosshair) and (center_y < self.height//2 + self.crosshair)): 
                print("FIRE CENTERED =========================") 
                self.isFireCentered.append(True) 
            else: 
                self.isFireCentered.append(False) 
            
        elif (self.state == 1) and (center_x == None) and (center_y == None): 
            print("No fire detected =============================")
            self.cmd_list.append("10") 
        
        # flame detecting mode 
        if self.state == 2: 
            print("flame detecting mode entered ================") 
            self.cmd_list.append("20") 

        # firing mode 
        if self.state == 3: 
            self.cmd_list.append("30") 

        # manual mode. 여기 처리해라. 
        if self.state == 4: 
            print("Manual mode entered ===================") 
            if manual_cmd: 
                print("Manual command sent!!! ========================") 
                self.cmd_list.append(manual_cmd) 
            else: 
                self.cmd_list.append("40") 
            
        
        
        # Send commands to arduino 
        cmd = ''.join(self.cmd_list) + '\n' 
        self.py_serial.write(cmd.encode()) 

        print("cmd:", cmd, " state:", self.state) 




if __name__ == "__main__": 
    motor = Motor() 

    while True: 
        center_x, center_y = motor.get_pred() 
        motor.read_ino() 
        motor.send_cmd(center_x, center_y) 
