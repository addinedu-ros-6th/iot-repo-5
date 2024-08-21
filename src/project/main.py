from PySide2.QtCore import Qt, QThread, Signal
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide2.QtGui import QImage, QPixmap
from ui_interface import *
from Custom_Widgets.Widgets import *
import cv2
import sys
import time

import motor_control_v2 as mc

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)

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
        self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        
        # CLOSE RIGHT MENU WIDGET
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())

        # CLOSE NOTIFICATION MENU WIDGET
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())

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

        # self.ui.pushButton_4.released.connect(self.stopClicked) 
        # self.ui.pushButton_3.released.connect(self.stopClicked) 
        # self.ui.pushButton_2.released.connect(self.stopClicked) 
        # self.ui.pushButton.released.connect(self.stopClicked) 

        self.manual_cmd = None 


    def test(self): 
        QMessageBox.information(self, "QMessageBox - information", "This is a test box.") 
    
    ###
    # Manual mode start 
    ###
    def convertToManual(self): 
        self.motor.state = 4 
    
    def convertToAuto(self): 
        self.motor.state = 0 
    
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
    ###
    # Manual mode stop 
    ###

    def updateCamera(self): 
        center_x, center_y, ret, frame = self.motor.get_pred() 
        self.motor.read_ino() 
        if (type(center_y) == int): 
            center_y = center_y - 50 
        self.motor.send_cmd(center_x, center_y, manual_cmd=self.manual_cmd) 
        
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