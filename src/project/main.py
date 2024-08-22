from PySide2.QtCore import Qt, QThread, Signal
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide2.QtGui import QImage, QPixmap
from ui_interface import *
from Custom_Widgets.Widgets import *
import cv2
import sys
import time
import webbrowser

import motor_control as mc

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
        self.blink_timer.timeout.connect(self.blink_card_6)
        # Set timer 11 secs
        self.auto_recover_timer = QTimer(self)
        self.auto_recover_timer.setSingleShot(True)
        self.auto_recover_timer.timeout.connect(self.convertToAuto)
        # After extinguited link to recover 0 status
        self.ui.fireAlertBtn.clicked.connect(self.convertToAuto)

        # intervaly check from Ino data
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_indicator)
        self.timer.start(100)

        self.manual_cmd = None 

    def update_indicator(self):
        self.motor.read_ino()
        if self.motor.deviceStatus == 1:
            self.set_indicator_color("green")
        else:
            self.set_indicator_color("grey")

    def set_indicator_color(self, color):
        # self.ui.label_20.setStyleSheet
        # (f"""
        #  QLabel {{
        #     background-color: {color};
        #     border-radius: 10px;
        #  }}
        #  """
        #  }})
        if color == "green":
            self.ui.indicator.setStyleSheet("background-color: rgb(0, 255, 0);")
        elif color == "grey":
            self.ui.indicator.setStyleSheet("background-color: rgb(128, 128, 128);")

    def blink_card_6(self):
        if self.blink_state:
            self.ui.card_6.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.blink_state = False
        else:
            self.ui.card_6.setStyleSheet("background-color: rgb(255, 0, 0);")
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
        self.test() 

    def fire_extinguished(self):
        if self.motor.state == 3:
            self.ui.popupNotificationContainer.expandMenu()
            self.blink_timer.stop()

            self.ui.label_13.setText("Fire Extinguished, Click the fireAlertBtn to return to Auto Patrol mode.")
            self.auto_recover_timer.start(11000)  # After 11 secs, recover to Auto

            # self.waterpumpOFF()

            self.blink_card_6.setStyleSheet("background-color: #343b47;")
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
        ip = "125.248.24.136"
        port = "8000"
        url = f"http://{ip}:{port}/login"
        webbrowser.open(url)



    ####
    # Manual mode start 
    ##
    def convertToManual(self): 
        self.motor.state = 4 
    
    def convertToAuto(self): 
        self.motor.state = 0
        self.ui.card_6.setStyleSheet("background-color: #343b47;")
        
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


# Execute App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())