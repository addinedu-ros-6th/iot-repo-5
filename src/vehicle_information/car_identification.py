import cv2
from ultralytics import YOLO
import numpy as np
import serial 
import mysql.connector
import easyocr
import re
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime


## Parking lot Entry - Vehicle Indentification

class GateCam:
    def __init__(self):
        self.vehicleTypeModel = YOLO("../../data/vehicle_yolov8s_best.pt")
        self.plateModel = YOLO("../../data/plate_yolov8s_best.pt")

        # Arduino Serial 통신 연결
        self.py_serial = serial.Serial(
            port='/dev/ttyACM0', 
            baudrate=9600, 
            timeout=1 
        )

        # mySQL 연결
        self.dbConnection = mysql.connector.connect(
            host = "125.248.24.136", 
            user = "remote",
            password = "1",
            database= "smart_fire_response_system"
        )

        # Webcam settings
        self.cap =  cv2.VideoCapture(0) # external cam : 2?
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)

        # 자체 상태 정보 (번호판, 차량 인식 상태)
        self.maxVehicleType = None
        self.maxPlate = None
        self.plateText = ""
        
        self.cmd_list = []
        self.count = 0
        self.resetCount = 90

        # OCR 모델 로드
        self.reader = easyocr.Reader(['ko', 'en'])  # 한국어, 영어, 숫자 인식        
        self.THRESHOLD = 0.7  # 신뢰도 임계값 설정
        
        # "숫자-한글-숫자" 패턴에 맞는지 확인하는 정규식
        self.pattern = re.compile(r'\d+\s*[가-힣]+\s*\d+')
        
        
    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()
        self.dbConnection.close()

    def visualize_results(self, frame, results, color):
        boxes = results[0].boxes.xyxy.cpu().numpy().astype(int)
        classes = results[0].boxes.cls.cpu().numpy().astype(int)

        label = None
        # 각 감지된 객체에 대해
        for box, cls in zip(boxes, classes):
            # 바운딩 박스 그리기
            cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), color, 2)

            # 클래스 이름과 신뢰도 점수 가져오기
            label = f"{results[0].names[cls]}"
            confidence = results[0].boxes.conf[0]

            # 레이블 텍스트 그리기
            cv2.putText(frame, f"{label} {confidence:.2f}", (box[0], box[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        return frame, label
        
    def frame_analysis(self):
        ret, frame = self.cap.read()
        if not ret:
            return
        
        self.cmd_list = [] 
        
        # 차량 인식 및 type 검출 
        vehicleTypeResults = self.vehicleTypeModel.predict(source=frame,  imgsz=640, conf=0.90, verbose=False)
        frame, vehicleType = self.visualize_results(frame, vehicleTypeResults, (255, 0, 0))

        # 번호판 인식
        plateResults = self.plateModel.predict(source=frame,  imgsz=640, conf=0.85, verbose=False)
        frame, plate = self.visualize_results(frame, plateResults, (0, 0, 255))

        if vehicleType is not None:
            # print(vehicleType)
            self.maxVehicleType = vehicleType

        if plate is not None:
            # print(plate)
            self.maxPlate = plate
        
        # OCR 수행
        result = self.reader.readtext(frame)

        # 프레임을 PIL 이미지로 변환
        frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(frame_pil)

        # 인식 결과 표시
        for bbox, text, conf in result:
            # 신뢰도가 임계값보다 높고, 텍스트가 "숫자-한글-숫자" 패턴에 맞는 경우만 처리
            if conf > self.THRESHOLD and self.pattern.match(text):
                self.plateText = text
                print(f"인식된 텍스트: {self.plateText} (신뢰도: {conf:.2f})")
                # 인식된 텍스트를 감싸는 박스를 그립니다.
                cv2.rectangle(frame, 
                              pt1=(int(bbox[0][0]), int(bbox[0][1])), 
                              pt2=(int(bbox[2][0]), int(bbox[2][1])), 
                              color=(0, 255, 0), thickness=3)
                # 인식된 텍스트를 화면에 표시합니다 (PIL 사용).
                # draw.text((int(bbox[0][0]), int(bbox[0][1]) - 40), text, fill=(0, 255, 0, 0))

        # PIL 이미지를 다시 OpenCV 이미지로 변환
        frame = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)

        cv2.imshow("Car Identification", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            return

    def send_cmd(self):
        if self.maxVehicleType is not None:
            self.cmd_list.append("1")
        else:
            self.cmd_list.append("0")

        if self.maxPlate is not None:
            self.cmd_list.append("1")
        else:
            self.cmd_list.append("0")
        
        if self.plateText is not "":
            self.cmd_list.append("1")
        else:
            self.cmd_list.append("0")

        cmd = ''.join(self.cmd_list) + "\n"
        # print(cmd)
        self.py_serial.write(cmd.encode())

        if self.maxPlate == "electric vehicle" and len(self.plateText) > 0:
            self.maxVehicleType = "electric vehicle"
            self.count += 1
        elif self.maxPlate != None and self.maxVehicleType != None and len(self.plateText) > 0:
            if self.count >= self.resetCount:
                if self.maxPlate == "electric vehicle":
                    isEV = True
                else:
                    isEV = False 

                entryTime = datetime.now()   

                # Insert data into DB
                cursor = self.dbConnection.cursor()
                query = f"INSERT INTO vehicle_info (plate_number, type, is_electric, entry_time) VALUES ({self.plateText}, {self.maxVehicleType}, {isEV}, {entryTime})"
                cursor.execute(query)

                self.maxPlate = None
                self.maxVehicleType = None
                self.plateText = ""
                self.count = 0
            else:
                self.count += 1


if __name__ == "__main__":
    cam = GateCam()

    while True:
        cam.frame_analysis()
        cam.send_cmd()


