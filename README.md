# iot-repo-5
IoT 프로젝트 5조 저장소. 스마트 화재 대응 시스템

## 1. 프로젝트 소개
### 1.1 주제 선정 배경

![chungra](https://github.com/user-attachments/assets/1265b7c3-7b0d-4aaa-88e8-3191a9c88896)
링크 : [청라 전기차 화재](https://newautopost.co.kr/issue-plus/article/112302/)

최근 발생한 지하 주차장 내 전기자동차 화재 사건과 관련하여, 이런 상황에서 우리가 배운 Embedded 와 딥러닝 기술을 사용하여 좀더 빠르고 효율적으로 대처할 수 있지 않을까?

### 1.2 주요 구현 기능

####  소방 관제 관측 및 제어부
* 화재 감지 및 추적 
* 화재 진압
* 화재 종료 여부 자동 확인 
* 영상 송출 및 저장

#### 차량 정보 인식 유닛
* 진입 차량 정보 인식 및 저장  

#### 관제 센터
* 관리구역 모니터링 (입고 차량, 소방 등급, 영상 확인 등) 
 
### 1.3 시스템 구성도
#### HW 구성도
![2024-08-25 145149](https://github.com/user-attachments/assets/b110be3e-8d39-489d-9304-1b0e0b88db62)
#### SW 구성도
<img src="https://github.com/user-attachments/assets/4a1782c1-6575-4796-89d9-6c06e0d80a39" alt="2024-08-25 145158" style="width: 300px; height: auto;">

### 1.4 팀원 소개
![team](https://github.com/user-attachments/assets/6a176d04-6895-4f17-84f9-018e30873c3f)


### 1.5 활용기술
![tech](https://github.com/user-attachments/assets/ea22bbd9-a55e-4be5-9dc2-bd07b2cb7b97)


## 2. 구현 기능 및 관련 기술
### 2.1 소방 관제 관측 및 제어부 
#### 기능 리스트
* 화재 감지 및 추적
  * 모터 제어 및 실시간 영상 감시
  * 화재 이미지 및 열원 감지
  * 열원 분석 및 화재 등급 분류
  * 부저 및 알림
* 화재 진압
  * 진압 용수 분사
  * 물탱크 수위 확인
* 진화 여부 자동 판단 
  * 소화 여부 확인
  * 관제소 인터페이스
  * 열원 분석 및 화재 등급 분류
  * 부저 및 알림
* 기록 관리
  * 영상 녹화
  * 화재 진압 로그 기록

#### 동작

![modes](https://github.com/user-attachments/assets/1706da3f-d590-4b95-98ca-91339a03c3a5)


* Patrol (Auto & Manual)
  * 좌우로 회전 하면 해당 구역을 촬영한다. 
  * 만약 불꽃으로 판단되는 이미지가 검출된 경우,  Aiming 모드로 변경된다.
  * 해당 동작에서 관제 센터 (GUI) 에서 카메라의 수동 조작으로 특정 위치를 촬영할 수 있다. 
  
* Aminig
  * 자동으로 검출된 불꽃 이미지가 화면의 중앙에 위치하도로 카메라의 x축, y축 값을 조정한다. 
  
* Fire Detecting
  * 화면 중앙에 위치한 불꽃을 Flame Detector 를 사용하여 실제 열이 발생하는 불꽃인지, 아니면 단순 이미지인지 검증한다. 
  * 불꽃으로 판단되면 Firing(화재진압) 모드 로, 아니면 Patrol 모드로 상태를 변경한다.

* Firing
  * water pump 를 구동하여 해당 위치로 물을 분사하여 화재를 진압한다.
  * 동시에 관재 센터 및 현장 buzzer 를 통해 화재 발생을 알린다. 
  * 해당 모드 진입 시점 5초 전부터 자동으로 영상 저장을 시작한다.
  * 카메라와 Flame Detector 는 계속 동작 중으로 화재가 진압되었는지 여부를 계속 확인한다. 
  * 만약 더이상 불꽃 이미지와 열원이 검출되지 않을 경우, 우선 관제 센터에 이를 알린다. 관제 센터에서 이를 확인하여 water pump 의 동작을 멈출 수 있다.
  * 화재 진압이 완료되었음에도 일정시간 (5초) 이내로 관제 센터에서 응답이 없을 경우, 자체적으로 작업을 종료하고 Patrol 모드로 변경한다. 


#### 영상에서 화재 여부 판단 Deep Learning 기술 

![2024-08-25 150620](https://github.com/user-attachments/assets/ca5bcb06-c2a2-4181-a10c-bd2a1beb50ce)

#### 동작 영상

[![2024-08-25 150910](https://github.com/user-attachments/assets/c604ac49-8479-4052-b76e-c08e9a70ac9f)](https://youtu.be/M-kVZQwV53k?si=pDrhxhxfKx2R1Whs)

### 2.2 차량 정보 인식 유닛
#### 기능 리스트
* 입고된 차량에 대한 정보를 미리 수집하여, 화재 발생 시, 화재 발생 차량 정보를 기록 및 소방 관제 등급을 분리하여 관리할 수 있도록 한다. 
  * 차량 외관 종류 감지: 승용차(car), Large(Van), Truck, etc. 
  * (한국) 전기차 번호판 여부 감지
  * 번호판 문자 인식
  
#### 차량 외관 종류 감지 Deep Learning 기술

![2024-08-25 145412](https://github.com/user-attachments/assets/f11f4a7f-9d67-4bcb-ad05-ce2f24b2bc5d)

#### (한국) 전기차 번호판 여부 감지 Deep Learning 기술

![2024-08-25 145420](https://github.com/user-attachments/assets/9fdc33a5-72ba-4dd6-801d-055a0ce4dc22)


#### OCR 이미지 문자 인식을 사용한 차량 번호 인식

![2024-08-25 145425](https://github.com/user-attachments/assets/5309cf3e-6a60-49fe-b690-08f28e6eb6fc)

#### 동작 영상

[![2024-08-25 151444](https://github.com/user-attachments/assets/b413ac09-38ce-4f19-a030-bb35c75abd4f)](https://youtube.com/shorts/6xv1Lbo-ZPo?si=CQbAogQ_im5aq9Ey)

### 2.3 Database - ERD
![erd](https://github.com/user-attachments/assets/7528c4cc-5514-4559-b065-c429c905bde9)

### 2.4 관제 센터 (GUI)
#### 기능 리스트
* 관리구역 현황 모니터링 
  * 종류별 주차 차량 수
  * 실시간 소방 등급
  * 구역 내 영상 확인 (자동/수동)
  * 부저 및 알람 on/off

* 과거 기록 영상 시청 
  * 과거 화재 발생 및 기록된 영상 로드 및 실행

#### Home
![2024-08-25 145442](https://github.com/user-attachments/assets/f9906a64-d396-4b3b-b129-6907ec4699cf)

#### Log Data View 

* Real-time retrieval of DB logs transmitted through Arduino

![log_data_view png](https://github.com/user-attachments/assets/1c7f06ff-d6c0-4872-92d7-6346d7b5f18a)

#### Live Monitoring

![2024-08-25 152109](https://github.com/user-attachments/assets/f08081ac-d24f-445a-8c81-202ada3e2a0b)

#### Recording File View 
[![2024-08-25 152109](https://github.com/user-attachments/assets/f08081ac-d24f-445a-8c81-202ada3e2a0b)](https://youtu.be/YKAlNO8vtrQ?si=kuCn69f-f6YmssA0)

#### Various User Interface

![screen1](https://github.com/user-attachments/assets/7004a9fa-4d75-47a1-a539-908273c8df62)

#### 소방 시스템 동작 중 영상

[![2024-08-25 152724](https://github.com/user-attachments/assets/9d8acd5d-e29e-477a-862c-a34c8eda05ea)](https://youtu.be/hH23VZV-6LM?si=iiM9x-hZtJJXsXXB)