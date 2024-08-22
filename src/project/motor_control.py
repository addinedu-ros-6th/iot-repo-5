import cv2
from ultralytics import YOLO
import numpy as np
import serial 
import time 
from collections import deque 


# 아두이노 연결 안되있거나 웹캠 연결 안되있는 경우 버전 
'''
TODO: 
- Process exceptions. 
- #1. 조준모드에서 불 안보이면 보일때까지 가만히 있는 예외 
- #2. 불 감지 모드에서 불 안보이면 가만히 있는 예외 
- #3. 수동모드에서 빠져나올때 펌프 켜져있거나 하는 등의 예외 처리하기 
- 아두이노 연결 안되있어도 프로그램은 실행되게 하기 
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
        # self.cap = cv2.VideoCapture(2) 
        self.cap = cv2.VideoCapture(0) 
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 640 480 
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH) 
        self.offset_x = 120 
        self.offset_y = 90
        self.crosshair = 40

        # 상태 전환 설정 
        self.state = 0 
        self.state_prev = 0 
        self.status_frames = 10 
        self.flame_frames = 20 
        self.isFireList = deque(maxlen=self.status_frames) 
        self.isFireCentered = deque(maxlen=self.status_frames) 
        self.isFlameSensor = deque(maxlen=self.flame_frames) 

        # 데이터 수신 
        self.deviceStatus = 0 
        self.ino_time = 0 
        self.position_x = 0 
        self.position_y = 0 
        self.direction_x = 0 
        self.direction_y = 0 
        self.motorStatus = 0 
        self.flameStatus = 0 
        self.waterStatus = 0 
    
    def __del__(self): 
        self.cap.release() 
        cv2.destroyAllWindows() 
    
    def get_pred(self): 
        ret, frame = self.cap.read() 
        if not ret: 
            return 

        results = self.model.predict(source=frame, imgsz=640, conf=0.7, verbose=False) 
        # results = self.model.predict(source=frame, imgsz=640, conf=0.9, verbose=False) 

        max_area = 0 
        max_box = None 
        
        for r in results: 
            boxes = r.boxes.xyxy.cpu().numpy() 
            confidences = r.boxes.conf.cpu().numpy() 
            classes = r.boxes.cls.cpu().numpy() 
            for box, _, _ in zip(boxes, confidences, classes): 
                x1, y1, x2, y2 = map(int, box) 
                area = (x2 - x1) * (y2 - y1) 
                if area > max_area:
                    max_area = area 
                    max_box = box 
        
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
                
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
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
        if self.py_serial.readable(): 
            response = self.py_serial.read_until(b'\n') 
            print("response:", response) 
            print() 

            self.deviceStatus = response[0] 
            self.ino_time = int.from_bytes(response[1:5], 'little') 
            self.position_x = response[5] 
            self.position_y = response[6] 
            self.direction_x = response[7] 
            self.direction_y = response[8] 
            self.motorStatus = response[9] 
            self.flameStatus = response[10] 
            self.waterStatus = response[11] 
        
        # 여기 테스트 필요 
        # else: 
        #     self.deviceStatus = 0 
        #     self.ino_time = 0 
        #     self.position_x = 0 
        #     self.position_y = 0 
        #     self.direction_x = 0 
        #     self.direction_y = 0 
        #     self.motorStatus = 0 
        #     self.flameStatus = 0 
        #     self.waterStatus = 0 
    
    def send_cmd(self, center_x, center_y, manual_cmd=None): 
        ## State transition part 
        self.state_prev = self.state 

        print("isFireList:", self.isFireList) 
        print("isFireCentered:", self.isFireCentered) 
        print("isFlameSensor:", self.isFlameSensor) 
        print() 

        # isFireList에 False가 없으면 1번 상태로 전환 
        if (self.state == 0) and (len(self.isFireList) == self.status_frames) and (False not in self.isFireList): 
            self.state = 1 
        
        # isFireCentered에 False가 없으면 2번 상태로 전환
        # isFireCentered에 True가 없으면 0번 상태로 전환  
        if (self.state == 1) and (len(self.isFireCentered) == self.status_frames) and (False not in self.isFireCentered): 
            self.state = 2 
        elif (self.state == 1) and (len(self.isFireList) == self.status_frames) and (True not in self.isFireList): 
            self.isFireCentered.clear() 
            self.isFlameSensor.clear() 
            self.state = 0
        
        # 불꽃센서가 한번이라도 반응하면 3번 상태로 전환 
        # isFlameSensor에 True가 없으면 0번 상태로 전환 
        if (self.state == 2) and self.flameStatus: 
            self.state = 3 
        elif (self.state == 2) and (len(self.isFlameSensor) == self.flame_frames) and (True not in self.isFlameSensor): 
            self.isFireCentered.clear() 
            self.isFlameSensor.clear() 
            self.state = 0 
        
        # isFireList에 True가 없으면 0번 상태로 전환 
        if (self.state == 3) and (True not in self.isFireList): 
            self.isFireCentered.clear() 
            self.isFlameSensor.clear() 
            self.state = 0 
        
        # 4번 상태로 가는 전환이나 빠져나가는 전환은 여기서 처리 안하므로 작성 내용이 없다 
        if (self.state == 4): 
            pass 


        ## Command part 
        self.cmd_list = [] 
        
        # patrol mode 
        if self.state == 0: 
            self.cmd_list.append("00") 
        
        # aiming mode 
        if ((self.state == 1) or (self.state == 3)) and center_x: 
            # 대략적인 위치로 회전
            if center_x < (self.width//2 - self.offset_x): 
                self.cmd_list.append("11") 
            elif center_x > (self.width//2 + self.offset_x): 
                self.cmd_list.append("12") 
            
            if center_y < (self.height//2 - self.offset_y): 
                self.cmd_list.append("13") 
            elif center_y > (self.height//2 + self.offset_y): 
                self.cmd_list.append("14") 

            # 자세한 위치로 회전 
            if (center_x >= (self.width//2 - self.offset_x)) and (center_x < self.width//2): 
                self.cmd_list.append("15") 
            elif (center_x <= (self.width//2 + self.offset_x)) and (center_x > self.width//2): 
                self.cmd_list.append("16") 
            
            if (center_y >= (self.height//2 - self.offset_y)) and (center_y < self.height//2): 
                self.cmd_list.append("17") 
            elif (center_y <= (self.height//2 + self.offset_y)) and (center_y > self.height//2): 
                self.cmd_list.append("18") 
            
            # 조준 완료 확인 
            if ((center_x > self.width//2 - self.crosshair) and (center_x < self.width//2 + self.crosshair)) and \
                    ((center_y > self.height//2 - self.crosshair) and (center_y < self.height//2 + self.crosshair)): 
                self.isFireCentered.append(True) 
            else: 
                self.isFireCentered.append(False) 
            
        elif (self.state == 1) and (center_x == None) and (center_y == None): 
            self.cmd_list.append("10") 
        
        # flame detecting mode 
        if self.state == 2: 
            self.cmd_list.append("20") 
            if self.flameStatus: 
                self.isFlameSensor.append(True) 
            else: 
                self.isFlameSensor.append(False) 

        # firing mode 
        if self.state == 3: 
            self.cmd_list.append("30") 

        # manual mode 
        if self.state == 4: 
            if manual_cmd: 
                self.cmd_list.append(manual_cmd) 
            else: 
                self.cmd_list.append("40") 
            
        
        
        # Send commands to arduino 
        cmd = ''.join(self.cmd_list) + '\n' 
        self.py_serial.write(cmd.encode()) 

        print("cmd:", cmd[:-1], "state:", self.state, "state_prev:", self.state_prev) 

        print("deviceStatus:", self.deviceStatus, "\tino_time:", self.ino_time, "\tpos_x:", self.position_x, "\tpos_y:", self.position_y)
        print("dir_x:", self.direction_x, "\tdir_y:", self.direction_y, "\tmotorStatus:", self.motorStatus, "\tflameStatus:", self.flameStatus, "\twaterStatus:", self.waterStatus) 
        print() 
        print() 




if __name__ == "__main__": 
    motor = Motor() 

    while True: 
        center_x, center_y = motor.get_pred() 
        motor.read_ino() 
        motor.send_cmd(center_x, center_y) 
