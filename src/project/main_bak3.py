from PySide2.QtCore import Qt, QThread, Signal, QTimer, QEventLoop
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from PySide2.QtGui import QImage, QPixmap
from ui_interface import *
from Custom_Widgets.Widgets import *
import cv2
import sys
import time
import webbrowser
import motor_control_bak3 as mc

'''
<Readme>
- 가상환경에서 'pip install -r requirements.txt' 실행하여 필요 패키지 깔기. 
  => opencv-python-headless가 아니라 opencv-python이 깔려있는지 주의. 헤드리스 써야함. 
- 아두이노 연결하여 motor_control_vO 파일 업로드. 
- 내장 웹캠을 사용하면 motor_control.py 파일의 cv2.VideoCapture(0) 사용. 
- 외부 웹캠을 사용하면 cv2.VideoCapture(2) 사용. 
- 
'''

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)  # Apply JSON Style

        self.show()

        # Initialize camera 
        self.motor = mc.Motor() 

        # Camera settings 
        self.camera = Camera(self) 
        self.camera.daemon = True 

        self.camera.running = True 
        self.camera.start() 

        self.camera.update.connect(self.updateCamera)  # 쓰레드에서 보낸 신호 받으면 self.updateCamera 함수 실행 

        # EXPAND CENTER MENU WIDGET SIZE
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        
        # CLOSE CENTER MENU WIDGET
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())

        # EXPAND RIGHT MENU WIDGET SIZE
        # self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        
        # CLOSE RIGHT MENU WIDGET
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())

        # CLOSE NOTIFICATION MENU WIDGET
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())

        # OPEN URL for Web Monitoring
        self.ui.profileMenuBtn.clicked.connect(self.open_webpage)

        # Manual mode buttons 
        self.ui.pushButton_8.clicked.connect(self.convertToManual)  # 메뉴얼 모드 전환 버튼 
        self.ui.pushButton_7.clicked.connect(self.convertToAuto)  # 자동 모드 전환 버튼 

        self.ui.pushButton_9.clicked.connect(self.waterpumpON)  # 메뉴얼 모드 펌프 키기
        self.ui.pushButton_10.clicked.connect(self.waterpumpOFF)  # 메뉴얼 모드 펌프 끄기 

        self.ui.pushButton_4.clicked.connect(self.leftClicked) 
        self.ui.pushButton_3.clicked.connect(self.rightClicked) 
        self.ui.pushButton_2.clicked.connect(self.upClicked) 
        self.ui.pushButton.clicked.connect(self.downClicked) 
        self.ui.pushButton_12.clicked.connect(self.stopClicked) 

        # Blink settings
        self.blink_timer = QTimer(self)
        self.blink_state = False
        self.blink_timer.timeout.connect(self.blink_card_5)

        # Set timer 11 secs
        self.auto_recover_timer = QTimer(self)
        self.auto_recover_timer.setSingleShot(True)
        self.auto_recover_timer.timeout.connect(self.convertToAuto)
        # After extinguited link to recover 0 status
        
        self.ui.fireAlertBtn.clicked.connect(self.convertToAuto)

        # # intervaly check from Ino data
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.update_indicator)
        # self.timer.start(1000)

        # Video controls
        self.ui.pushButton_11.clicked.connect(self.open_video_file)
        self.ui.playBtn.clicked.connect(self.play_video)
        self.ui.pauseBtn.clicked.connect(self.pause_video)
        self.ui.stopBtn.clicked.connect(self.stop_video)
        self.ui.zoomInBtn.clicked.connect(self.zoom_in)
        self.ui.zoomOutBtn.clicked.connect(self.zoom_out)

        self.video_player = None
        self.current_video_path = None
        self.zoom_factor = 1.0  # 초기 줌 배율 설정
        self.max_zoom = 4.0  # 최대 줌 배율
        self.min_zoom = 1.0  # 최소 줌 배율

        self.manual_cmd = None 

    def update_indicator(self):
        # self.motor.read_ino()
        if self.motor.deviceStatus == 1:
            self.set_indicator_color("green")
        else:
            self.set_indicator_color("gray")

    def set_indicator_color(self, color):
        self.ui.label_20.setStyleSheet(f"""
         QLabel {{
            background-color: {color};
            border-radius: 10px;
         }}
         """)
        # if color == "green":
        #     self.ui.indicator.setStyleSheet("background-color: rgb(0, 255, 0);")
        # elif color == "grey":
        #     self.ui.indicator.setStyleSheet("background-color: rgb(128, 128, 128);")

    def blink_card_5(self):
        if self.blink_state:
            self.ui.card_5.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.blink_state = False
        else:
            self.ui.card_5.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.blink_state = True

    def fire_detected(self):
        # if self.motor.state == 3:
        #     self.ui.popupNotificationContainer.expandMenu()
        #     self.blink_timer.start(500)
        #     self.ui.label_13.setText("Fire Detected")
        # else:
        #     pass
        self.ui.popupNotificationContainer.expandMenu()
        self.blink_timer.start(500)
        self.ui.label_13.setText("Fire Detected")
        self.motor.start_recording()

    def fire_extinguished(self):
        if self.motor.state == 0:
            self.ui.popupNotificationContainer.expandMenu()
            self.blink_timer.stop()

            self.ui.label_13.setText("Fire Extinguished, Click the fireAlertBtn to return to Auto Patrol mode.")
            self.auto_recover_timer.start(11000)  # After 11 secs, recover to Auto

            # self.waterpumpOFF()
            self.motor.stop_recording()

            self.blink_card_5.setStyleSheet("background-color: #343b47;")
        else:
            pass

    def auto_recover(self):
        # After 11 secs, if there is no confirmation, recover to Auto
        self.ui.label_13.setText("Return to Patrol Auto Mode")
        self.convertToAuto()

    def user_initiated_recover(self):
        # if there is confirmation with user, recover to Auto
        if self.auto_recover_timer.isActive():
            self.auto_recover_timer.stop()  # Stop timer
        self.convertToAuto()


    def test(self): 
        QMessageBox.information(self, "QMessageBox - information", "This is a test box.") 
    
    def open_webpage(self):
        # ip = "125.248.24.136"
        ip = "localhost"
        port = "8000"
        url = f"http://{ip}:{port}/login"
        webbrowser.open(url)

        # Set a timer to quit the application after opening the browser
        QTimer.singleShot(10, QApplication.quit)  # 10ms 후 애플리케이션 종료


    ####
    # Manual mode start 
    ##
    def convertToManual(self): 
        self.motor.state = 4 
    
    def convertToAuto(self): 
        self.motor.state = 0
        self.ui.card_5.setStyleSheet("background-color: #343b47;")
        
    def check_fire_status(self, isFireCentered, isFlameSensor):
        if isFireCentered and isFlameSensor:
            self.fire_detected()
        elif not isFireCentered and not isFlameSensor:
            self.fire_extinguished()
    
    def waterpumpON(self): 
        if self.motor.state == 4: 
            self.manual_cmd = "41" 
    
    def waterpumpOFF(self): 
        if self.motor.state == 4: 
            self.manual_cmd = "42" 

    def leftClicked(self): 
        if self.motor.state == 4: 
            print("leftClicked func called!!!") 
            self.manual_cmd = "11" 

    def rightClicked(self): 
        if self.motor.state == 4: 
            print("rightClicked func called!!!") 
            self.manual_cmd = "12" 

    def upClicked(self): 
        if self.motor.state == 4: 
            print("upClicked func called!!!") 
            self.manual_cmd = "13" 

    def downClicked(self): 
        if self.motor.state == 4: 
            print("downClicked func called!!!") 
            self.manual_cmd = "14" 
        
    def stopClicked(self): 
        if self.motor.state == 4: 
            print("stopClicked func called!!!") 
            self.manual_cmd = None 
    ##
    # Manual mode stop 
    ####

    def updateCamera(self): 
        center_x, center_y, ret, frame = self.motor.get_pred() 
        self.motor.read_ino() 
        self.motor.send_cmd(center_x, center_y, manual_cmd=self.manual_cmd) 
        self.update_indicator() 

        # 여기 테스트 필요 
        if (self.motor.state_prev == 2) and (self.motor.state == 3): 
            self.fire_detected() 
        elif (self.motor.state_prev == 3) and (self.motor.state == 0): 
            self.fire_extinguished() 

        if ret: 
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 

            h, w, c = frame.shape 
            qimage = QImage(frame.data, w, h, w*c, QImage.Format_RGB888) 

            self.pixmap_home = QPixmap.fromImage(qimage) 
            self.pixmap_home = self.pixmap_home.scaled(self.ui.smallMonitorLabel.width(), self.ui.smallMonitorLabel.height()) 

            self.pixmap_monitor = QPixmap.fromImage(qimage) 
            self.pixmap_monitor = self.pixmap_monitor.scaled(self.ui.label_12.width(), self.ui.label_12.height()) 

            self.ui.smallMonitorLabel.setPixmap(self.pixmap_home) 
            self.ui.label_12.setPixmap(self.pixmap_monitor) 

    # 비디오 파일 선택 및 썸네일 설정
    def open_video_file(self):
        video_file, _ = QFileDialog.getOpenFileName(self, "Select Video File", "./videos", "Video Files (*.mp4 *.avi *.mov)")
        if video_file:
            self.current_video_path = video_file
            self.set_video_thumbnail(video_file)

    # 썸네일 이미지 설정
    def set_video_thumbnail(self, video_file):
        cap = cv2.VideoCapture(video_file)
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, c = frame.shape
            qimage = QImage(frame.data, w, h, w * c, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qimage)
            self.ui.label_16.setPixmap(pixmap.scaled(self.ui.label_16.width(), self.ui.label_16.height()))
        cap.release()

    # 비디오 재생
    def play_video(self):
        if self.current_video_path:
            if self.video_player and self.video_player.isRunning():
                self.video_player.resume()
            else:
                self.video_player = VideoPlayer(self.current_video_path, self)
                self.video_player.update_frame.connect(self.update_video_frame)
                self.video_player.start()

    # 비디오 일시정지
    def pause_video(self):
        if self.video_player:
            self.video_player.pause()

    # 비디오 정지 및 썸네일로 복귀
    def stop_video(self):
        if self.video_player:
            self.video_player.stop()
            self.set_video_thumbnail(self.current_video_path)

    # 비디오 프레임 업데이트
    def update_video_frame(self, qimage):
        pixmap = QPixmap.fromImage(qimage)
        self.ui.label_16.setPixmap(pixmap.scaled(self.ui.label_16.width() * self.zoom_factor, 
                                                 self.ui.label_16.height() * self.zoom_factor))

    # Zoom In
    def zoom_in(self):
        if self.zoom_factor < self.max_zoom:
            self.zoom_factor *= 1.2  # 줌 인 시 배율 증가
            self.apply_zoom()

    # Zoom Out
    def zoom_out(self):
        if self.zoom_factor > self.min_zoom:
            self.zoom_factor /= 1.2  # 줌 아웃 시 배율 감소
            self.apply_zoom()

    # 줌 적용
    def apply_zoom(self):
        if self.video_player and self.video_player.isRunning():
            self.video_player.update_frame.connect(self.update_video_frame)  # 실시간 줌 적용
        else:
            pixmap = self.ui.label_16.pixmap()
            if pixmap:
                self.ui.label_16.setPixmap(pixmap.scaled(self.ui.label_16.width() * self.zoom_factor, 
                                                         self.ui.label_16.height() * self.zoom_factor, 
                                                         Qt.KeepAspectRatio))

class Camera(QThread): 
    update = Signal() 

    def __init__(self, parent=None): 
        super().__init__(parent)
        self.running = True 
    
    def run(self): 
        while self.running == True: 
            self.update.emit() 
            time.sleep(0.05) 
    
    def stop(self): 
        self.running = False    


class VideoPlayer(QThread):
    update_frame = Signal(QImage)

    def __init__(self, video_path, parent=None):
        super().__init__(parent)
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.is_paused = False
        self.is_stopped = False
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)  # 비디오의 프레임 속도 가져오기
        self.delay = int(1000 / self.fps)  # 프레임 간 대기 시간을 계산

    def run(self):
        while self.cap.isOpened():
            if self.is_stopped:
                break
            if not self.is_paused:
                ret, frame = self.cap.read()
                if ret:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    h, w, c = frame.shape
                    qimage = QImage(frame.data, w, h, w * c, QImage.Format_RGB888)
                    self.update_frame.emit(qimage)
                    self.msleep(self.delay)  # 각 프레임 사이에 FPS에 맞춰 대기 시간을 추가하여 재생 속도를 조절
                else:
                    break
            else:
                QEventLoop().processEvents()  # Pause while loop

        self.cap.release()

    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False

    def stop(self):
        self.is_stopped = True


# Execute App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())