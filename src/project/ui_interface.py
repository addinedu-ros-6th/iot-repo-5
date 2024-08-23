# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceMowcFC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(957, 527)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #1f232a;\n"
"}\n"
"#leftMenuSubContainer{\n"
"	background-color: #16191d;\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"#centerMenuSubContainer, #rightMenuSubContainer{\n"
"	background-color: #2c313c;\n"
"}\n"
"#frame_4, #frame_8, #popupNotificationSubContainer{\n"
"	background-color: #16191d;\n"
"	border-radius: 10px;\n"
"}\n"
"#headerContainer, #footerContainer{\n"
"	background-color: #2c313c;\n"
"}\n"
"#card_1, #card_2, #card_3, #card_4, #controlBtnLayout, #zoomInOutBtnFrame, #card_5, #card_6, #frame_17, #frame_19\n"
"{\n"
"	background-color: #343b47;\n"
"	border-radius: 20px;\n"
"}\n"
"#label_20\n"
"{\n"
"	border-radius: 10px;\n"
"	background-color: gray;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMaximumSize(QSize(45, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/whiteIcons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeBtn.setStyleSheet(u"background-color: #1f232a;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/whiteIcons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.dataBtn = QPushButton(self.frame_2)
        self.dataBtn.setObjectName(u"dataBtn")
        self.dataBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/whiteIcons/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dataBtn.setIcon(icon2)
        self.dataBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.dataBtn)

        self.monitorBtn = QPushButton(self.frame_2)
        self.monitorBtn.setObjectName(u"monitorBtn")
        self.monitorBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/whiteIcons/monitor.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.monitorBtn.setIcon(icon3)
        self.monitorBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.monitorBtn)

        self.reviewBtn = QPushButton(self.frame_2)
        self.reviewBtn.setObjectName(u"reviewBtn")
        self.reviewBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/whiteIcons/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.reviewBtn.setIcon(icon4)
        self.reviewBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.reviewBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/whiteIcons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon5)
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.frame_3)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/whiteIcons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon6)
        self.infoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/whiteIcons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon7)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.closeCenterMenuBtn = QPushButton(self.frame_4)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.closeCenterMenuBtn.sizePolicy().hasHeightForWidth())
        self.closeCenterMenuBtn.setSizePolicy(sizePolicy2)
        self.closeCenterMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeCenterMenuBtn.setLayoutDirection(Qt.LeftToRight)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/whiteIcons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon8)
        self.closeCenterMenuBtn.setIconSize(QSize(24, 24))
        self.closeCenterMenuBtn.setAutoExclusive(False)

        self.horizontalLayout_4.addWidget(self.closeCenterMenuBtn)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.centerMenuPages = QCustomStackedWidget(self.centerMenuSubContainer)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.centerMenuPages.setFont(font)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(13)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_3)

        self.centerMenuPages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_4)

        self.textEdit = QTextEdit(self.page_2)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_8.addWidget(self.textEdit)

        self.centerMenuPages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_5)

        self.textEdit_2 = QTextEdit(self.page_3)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.verticalLayout_9.addWidget(self.textEdit_2)

        self.centerMenuPages.addWidget(self.page_3)

        self.verticalLayout_6.addWidget(self.centerMenuPages)


        self.verticalLayout_5.addWidget(self.centerMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.mainBodyContainer.setMinimumSize(QSize(710, 527))
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_6 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(32, 32))
        self.label_6.setPixmap(QPixmap(u":/images/logo/fire-hydrant.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_7)


        self.horizontalLayout_6.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.notificationBtn = QPushButton(self.frame_6)
        self.notificationBtn.setObjectName(u"notificationBtn")
        self.notificationBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/whiteIcons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon9)
        self.notificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.notificationBtn)

        self.moreMenuBtn = QPushButton(self.frame_6)
        self.moreMenuBtn.setObjectName(u"moreMenuBtn")
        self.moreMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/whiteIcons/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moreMenuBtn.setIcon(icon10)
        self.moreMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.moreMenuBtn)

        self.profileMenuBtn = QPushButton(self.frame_6)
        self.profileMenuBtn.setObjectName(u"profileMenuBtn")
        self.profileMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/whiteIcons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileMenuBtn.setIcon(icon11)
        self.profileMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.profileMenuBtn)


        self.horizontalLayout_6.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/whiteIcons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon12)

        self.horizontalLayout_5.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/whiteIcons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon13)

        self.horizontalLayout_5.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/whiteIcons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon14)

        self.horizontalLayout_5.addWidget(self.closeBtn)


        self.horizontalLayout_6.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy3)
        self.horizontalLayout_3 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.verticalLayout_15 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 0)
        self.mainPages = QCustomStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_16 = QVBoxLayout(self.page_6)
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.page_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_13)
        self.verticalLayout_22.setSpacing(20)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.card_1 = QFrame(self.frame_14)
        self.card_1.setObjectName(u"card_1")
        sizePolicy.setHeightForWidth(self.card_1.sizePolicy().hasHeightForWidth())
        self.card_1.setSizePolicy(sizePolicy)
        self.card_1.setFrameShape(QFrame.StyledPanel)
        self.card_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.card_1)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 5, 0)
        self.frame_32 = QFrame(self.card_1)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_30 = QLabel(self.frame_32)
        self.label_30.setObjectName(u"label_30")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_30.setFont(font3)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_30)

        self.label_32 = QLabel(self.frame_32)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(0, 0))
        self.label_32.setMaximumSize(QSize(35, 35))
        self.label_32.setPixmap(QPixmap(u":/icons/icons/whiteIcons/car_standard.svg"))
        self.label_32.setScaledContents(True)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_32)


        self.verticalLayout_23.addWidget(self.frame_32, 0, Qt.AlignTop)

        self.frame_31 = QFrame(self.card_1)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_31)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 10)
        self.label_29 = QLabel(self.frame_31)
        self.label_29.setObjectName(u"label_29")
        font4 = QFont()
        font4.setPointSize(30)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_29.setFont(font4)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_29)


        self.verticalLayout_23.addWidget(self.frame_31, 0, Qt.AlignTop)


        self.horizontalLayout_16.addWidget(self.card_1)

        self.card_2 = QFrame(self.frame_14)
        self.card_2.setObjectName(u"card_2")
        self.card_2.setFrameShape(QFrame.StyledPanel)
        self.card_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.card_2)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 5, 0)
        self.frame_34 = QFrame(self.card_2)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_34 = QLabel(self.frame_34)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font3)
        self.label_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_34)

        self.label_35 = QLabel(self.frame_34)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(0, 0))
        self.label_35.setMaximumSize(QSize(35, 35))
        self.label_35.setPixmap(QPixmap(u":/icons/icons/whiteIcons/car-bus-1.svg"))
        self.label_35.setScaledContents(True)
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_35)


        self.verticalLayout_24.addWidget(self.frame_34, 0, Qt.AlignTop)

        self.frame_33 = QFrame(self.card_2)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_33)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 10)
        self.label_33 = QLabel(self.frame_33)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font4)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.label_33, 0, Qt.AlignTop)


        self.verticalLayout_24.addWidget(self.frame_33, 0, Qt.AlignTop)


        self.horizontalLayout_16.addWidget(self.card_2)

        self.card_3 = QFrame(self.frame_14)
        self.card_3.setObjectName(u"card_3")
        self.card_3.setFrameShape(QFrame.StyledPanel)
        self.card_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.card_3)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 5, 0)
        self.frame_27 = QFrame(self.card_3)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_22 = QLabel(self.frame_27)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font3)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_22)

        self.label_23 = QLabel(self.frame_27)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 0))
        self.label_23.setMaximumSize(QSize(35, 35))
        self.label_23.setPixmap(QPixmap(u":/icons/icons/whiteIcons/truck.svg"))
        self.label_23.setScaledContents(True)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_23)


        self.verticalLayout_28.addWidget(self.frame_27, 0, Qt.AlignTop)

        self.frame_28 = QFrame(self.card_3)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_28)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 10)
        self.label_24 = QLabel(self.frame_28)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font4)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_24, 0, Qt.AlignTop)


        self.verticalLayout_28.addWidget(self.frame_28, 0, Qt.AlignTop)


        self.horizontalLayout_16.addWidget(self.card_3)

        self.card_4 = QFrame(self.frame_14)
        self.card_4.setObjectName(u"card_4")
        self.card_4.setFrameShape(QFrame.StyledPanel)
        self.card_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.card_4)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 5, 0)
        self.frame_29 = QFrame(self.card_4)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_25 = QLabel(self.frame_29)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font3)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_25)

        self.label_26 = QLabel(self.frame_29)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 0))
        self.label_26.setMaximumSize(QSize(35, 35))
        self.label_26.setPixmap(QPixmap(u":/icons/icons/whiteIcons/battery-charging.svg"))
        self.label_26.setScaledContents(True)
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_26)


        self.verticalLayout_30.addWidget(self.frame_29, 0, Qt.AlignTop)

        self.frame_30 = QFrame(self.card_4)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_30)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 10)
        self.label_27 = QLabel(self.frame_30)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font4)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_27, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_30.addWidget(self.frame_30, 0, Qt.AlignTop)


        self.horizontalLayout_16.addWidget(self.card_4)


        self.verticalLayout_22.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.card_5 = QFrame(self.frame_15)
        self.card_5.setObjectName(u"card_5")
        self.card_5.setFrameShape(QFrame.StyledPanel)
        self.card_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.card_5)
        self.verticalLayout_31.setSpacing(3)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 10, 0, 10)
        self.label_28 = QLabel(self.card_5)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_28, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.fireAlertBtn = QPushButton(self.card_5)
        self.fireAlertBtn.setObjectName(u"fireAlertBtn")
        self.fireAlertBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/pngicons/icons/pngIcons/fire-alarm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fireAlertBtn.setIcon(icon15)
        self.fireAlertBtn.setIconSize(QSize(80, 80))

        self.verticalLayout_31.addWidget(self.fireAlertBtn, 0, Qt.AlignTop)


        self.horizontalLayout_15.addWidget(self.card_5)

        self.card_6 = QFrame(self.frame_15)
        self.card_6.setObjectName(u"card_6")
        self.card_6.setFrameShape(QFrame.StyledPanel)
        self.card_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.card_6)
        self.verticalLayout_32.setSpacing(3)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 10, 0, 10)
        self.label_31 = QLabel(self.card_6)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_31, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.waterAlertBtn = QPushButton(self.card_6)
        self.waterAlertBtn.setObjectName(u"waterAlertBtn")
        self.waterAlertBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/pngicons/icons/pngIcons/water1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.waterAlertBtn.setIcon(icon16)
        self.waterAlertBtn.setIconSize(QSize(80, 80))

        self.verticalLayout_32.addWidget(self.waterAlertBtn, 0, Qt.AlignTop)


        self.horizontalLayout_15.addWidget(self.card_6)

        self.card_monitor = QFrame(self.frame_15)
        self.card_monitor.setObjectName(u"card_monitor")
        self.card_monitor.setFrameShape(QFrame.StyledPanel)
        self.card_monitor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.card_monitor)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.smallMonitorLabel = QLabel(self.card_monitor)
        self.smallMonitorLabel.setObjectName(u"smallMonitorLabel")
        self.smallMonitorLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.smallMonitorLabel)


        self.horizontalLayout_15.addWidget(self.card_monitor)


        self.verticalLayout_22.addWidget(self.frame_15)


        self.verticalLayout_16.addWidget(self.frame_13)

        self.mainPages.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_17 = QVBoxLayout(self.page_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.page_7)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_20)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.tableWidget = QTableWidget(self.frame_20)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_26.addWidget(self.tableWidget)

        self.refreshTableBtn = QPushButton(self.frame_20)
        self.refreshTableBtn.setObjectName(u"refreshTableBtn")
        self.refreshTableBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/whiteIcons/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshTableBtn.setIcon(icon17)
        self.refreshTableBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_26.addWidget(self.refreshTableBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_17.addWidget(self.frame_20)

        self.mainPages.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_18 = QVBoxLayout(self.page_8)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_12 = QLabel(self.page_8)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_12)

        self.frame_16 = QFrame(self.page_8)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setMaximumSize(QSize(450, 90))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy4)
        self.frame_17.setMaximumSize(QSize(16777215, 90))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.controlBtnLayout = QGridLayout()
        self.controlBtnLayout.setSpacing(0)
        self.controlBtnLayout.setObjectName(u"controlBtnLayout")
        self.label_10 = QLabel(self.frame_17)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.controlBtnLayout.addWidget(self.label_10, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_17)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/whiteIcons/arrow-up-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon18)
        self.pushButton_2.setIconSize(QSize(30, 30))
        self.pushButton_2.setAutoRepeat(True)

        self.controlBtnLayout.addWidget(self.pushButton_2, 1, 3, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton = QPushButton(self.frame_17)
        self.pushButton.setObjectName(u"pushButton")
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons/whiteIcons/arrow-down-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon19)
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton.setAutoRepeat(True)

        self.controlBtnLayout.addWidget(self.pushButton, 2, 3, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.pushButton_5 = QPushButton(self.frame_17)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon20 = QIcon()
        icon20.addFile(u":/icons/icons/whiteIcons/plus-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon20)
        self.pushButton_5.setIconSize(QSize(30, 30))
        self.pushButton_5.setAutoRepeat(True)

        self.controlBtnLayout.addWidget(self.pushButton_5, 1, 5, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.pushButton_4 = QPushButton(self.frame_17)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon21 = QIcon()
        icon21.addFile(u":/icons/icons/whiteIcons/arrow-left-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon21)
        self.pushButton_4.setIconSize(QSize(30, 30))
        self.pushButton_4.setAutoRepeat(True)

        self.controlBtnLayout.addWidget(self.pushButton_4, 2, 2, 1, 1, Qt.AlignRight|Qt.AlignTop)

        self.pushButton_3 = QPushButton(self.frame_17)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon22 = QIcon()
        icon22.addFile(u":/icons/icons/whiteIcons/arrow-right-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon22)
        self.pushButton_3.setIconSize(QSize(30, 30))
        self.pushButton_3.setAutoRepeat(True)

        self.controlBtnLayout.addWidget(self.pushButton_3, 2, 4, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.pushButton_8 = QPushButton(self.frame_17)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon23 = QIcon()
        icon23.addFile(u":/icons/icons/whiteIcons/on-rounded.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon23.addFile(u":/icons_orange/icons/orangIcons/on-rounded-clicked.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_8.setIcon(icon23)
        self.pushButton_8.setIconSize(QSize(35, 35))

        self.controlBtnLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.frame_17)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon24 = QIcon()
        icon24.addFile(u":/icons/icons/whiteIcons/off-rounded.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon24.addFile(u":/icons_orange/icons/orangIcons/off-rounded-clicked.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_7.setIcon(icon24)
        self.pushButton_7.setIconSize(QSize(35, 35))

        self.controlBtnLayout.addWidget(self.pushButton_7, 2, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.frame_17)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon25 = QIcon()
        icon25.addFile(u":/icons/icons/whiteIcons/minus-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon25)
        self.pushButton_6.setIconSize(QSize(30, 30))
        self.pushButton_6.setAutoRepeat(True)

        self.controlBtnLayout.addWidget(self.pushButton_6, 2, 5, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.pushButton_12 = QPushButton(self.frame_17)
        self.pushButton_12.setObjectName(u"pushButton_12")
        icon26 = QIcon()
        icon26.addFile(u":/icons/icons/whiteIcons/stop-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon26)
        self.pushButton_12.setIconSize(QSize(35, 35))

        self.controlBtnLayout.addWidget(self.pushButton_12, 2, 0, 1, 1)

        self.label_18 = QLabel(self.frame_17)
        self.label_18.setObjectName(u"label_18")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_18.setFont(font5)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.controlBtnLayout.addWidget(self.label_18, 1, 0, 1, 1)

        self.label_19 = QLabel(self.frame_17)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.controlBtnLayout.addWidget(self.label_19, 0, 0, 1, 1)


        self.horizontalLayout_18.addLayout(self.controlBtnLayout)


        self.horizontalLayout_17.addWidget(self.frame_17, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.frame_19 = QFrame(self.frame_16)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_19)
        self.verticalLayout_25.setSpacing(5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_19)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_17, 0, Qt.AlignTop)

        self.pushButton_9 = QPushButton(self.frame_19)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setIcon(icon23)
        self.pushButton_9.setIconSize(QSize(35, 35))

        self.verticalLayout_25.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.frame_19)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setIcon(icon24)
        self.pushButton_10.setIconSize(QSize(35, 35))

        self.verticalLayout_25.addWidget(self.pushButton_10)


        self.horizontalLayout_17.addWidget(self.frame_19)


        self.verticalLayout_18.addWidget(self.frame_16)

        self.mainPages.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_21 = QVBoxLayout(self.page_9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_11 = QFrame(self.page_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_16 = QLabel(self.frame_11)
        self.label_16.setObjectName(u"label_16")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy5)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_16)


        self.verticalLayout_21.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.page_9)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy6)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(100, 0, 100, 0)
        self.playBtn = QPushButton(self.frame_12)
        self.playBtn.setObjectName(u"playBtn")
        icon27 = QIcon()
        icon27.addFile(u":/icons/icons/whiteIcons/play-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.playBtn.setIcon(icon27)
        self.playBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.playBtn)

        self.pauseBtn = QPushButton(self.frame_12)
        self.pauseBtn.setObjectName(u"pauseBtn")
        icon28 = QIcon()
        icon28.addFile(u":/icons/icons/whiteIcons/pause-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pauseBtn.setIcon(icon28)
        self.pauseBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.pauseBtn)

        self.stopBtn = QPushButton(self.frame_12)
        self.stopBtn.setObjectName(u"stopBtn")
        self.stopBtn.setIcon(icon26)
        self.stopBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.stopBtn)

        self.zoomInBtn = QPushButton(self.frame_12)
        self.zoomInBtn.setObjectName(u"zoomInBtn")
        icon29 = QIcon()
        icon29.addFile(u":/icons/icons/whiteIcons/zoom-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.zoomInBtn.setIcon(icon29)
        self.zoomInBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.zoomInBtn)

        self.zoomOutBtn = QPushButton(self.frame_12)
        self.zoomOutBtn.setObjectName(u"zoomOutBtn")
        icon30 = QIcon()
        icon30.addFile(u":/icons/icons/whiteIcons/zoom-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.zoomOutBtn.setIcon(icon30)
        self.zoomOutBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.zoomOutBtn)

        self.pushButton_11 = QPushButton(self.frame_12)
        self.pushButton_11.setObjectName(u"pushButton_11")
        icon31 = QIcon()
        icon31.addFile(u":/icons/icons/whiteIcons/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon31)
        self.pushButton_11.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.pushButton_11)


        self.verticalLayout_21.addWidget(self.frame_12, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.mainPages.addWidget(self.page_9)

        self.verticalLayout_15.addWidget(self.mainPages)


        self.horizontalLayout_3.addWidget(self.mainContentsContainer)

        self.rightMenuContainer = QCustomSlideMenu(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_11 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_12 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.frame_8 = QFrame(self.rightMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label)

        self.closeRightMenuBtn = QPushButton(self.frame_8)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeRightMenuBtn.setIcon(icon8)
        self.closeRightMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.rightMenuPages = QCustomStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_13 = QVBoxLayout(self.page_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.page_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_8)

        self.rightMenuPages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_14 = QVBoxLayout(self.page_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.page_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)

        self.rightMenuPages.addWidget(self.page_5)

        self.verticalLayout_12.addWidget(self.rightMenuPages)


        self.verticalLayout_11.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_3.addWidget(self.rightMenuContainer, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.mainBodyContent)

        self.popupNotificationContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName(u"popupNotificationContainer")
        self.verticalLayout_19 = QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.popupNotificationSubContainer = QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName(u"popupNotificationSubContainer")
        self.verticalLayout_20 = QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_14 = QLabel(self.popupNotificationSubContainer)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.verticalLayout_20.addWidget(self.label_14)

        self.frame_9 = QFrame(self.popupNotificationSubContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_13)

        self.closeNotificationBtn = QPushButton(self.frame_9)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        self.closeNotificationBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon32 = QIcon()
        icon32.addFile(u":/icons/icons/whiteIcons/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeNotificationBtn.setIcon(icon32)
        self.closeNotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.closeNotificationBtn, 0, Qt.AlignRight)


        self.verticalLayout_20.addWidget(self.frame_9)


        self.verticalLayout_19.addWidget(self.popupNotificationSubContainer)


        self.verticalLayout_10.addWidget(self.popupNotificationContainer)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.horizontalLayout_11 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.footerContainer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")
        font6 = QFont()
        font6.setBold(False)
        font6.setItalic(True)
        font6.setWeight(50)
        self.label_15.setFont(font6)

        self.horizontalLayout_12.addWidget(self.label_15)


        self.horizontalLayout_11.addWidget(self.frame_10)

        self.frame_18 = QFrame(self.footerContainer)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_20 = QLabel(self.frame_18)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(20, 20))
        self.label_20.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_23.addWidget(self.label_20, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_11.addWidget(self.frame_18)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(30, 30))
        self.sizeGrip.setMaximumSize(QSize(30, 30))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.sizeGrip, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.footerContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerMenuPages.setCurrentIndex(2)
        self.mainPages.setCurrentIndex(1)
        self.pushButton_2.setDefault(True)
        self.pushButton.setDefault(True)
        self.pushButton_4.setDefault(True)
        self.pushButton_3.setDefault(True)
        self.rightMenuPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.dataBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Data Storage", None))
#endif // QT_CONFIG(tooltip)
        self.dataBtn.setText(QCoreApplication.translate("MainWindow", u"Review Data", None))
#if QT_CONFIG(tooltip)
        self.monitorBtn.setToolTip(QCoreApplication.translate("MainWindow", u"CCTV", None))
#endif // QT_CONFIG(tooltip)
        self.monitorBtn.setText(QCoreApplication.translate("MainWindow", u"Monitoring", None))
#if QT_CONFIG(tooltip)
        self.reviewBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Play Recorded Files", None))
#endif // QT_CONFIG(tooltip)
        self.reviewBtn.setText(QCoreApplication.translate("MainWindow", u"Video", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to setting", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Information about the app", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Get more help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Smart Fire Response", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">We do protect your property from the initial fire.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ver. 100.24.001</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Contact</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Video Sys Manager: Sehyoung Lee</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent"
                        ":0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">DL &amp; Data Manager: Yonggon Yoon</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sehyoung Lee</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sensing &amp; Hardware Equip. Manager: Kiwook Kim</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:"
                        "0px; -qt-block-indent:0; text-indent:0px;\">Oper Sys Manager: JooYoen Kim</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Joo_K</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Interface &amp; DB Manager: Joo_K</p></body></html>", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"SFR System", None))
#if QT_CONFIG(tooltip)
        self.notificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Notification list", None))
#endif // QT_CONFIG(tooltip)
        self.notificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.moreMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.moreMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.profileMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Web Monitoring Connection", None))
#endif // QT_CONFIG(tooltip)
        self.profileMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Standard", None))
        self.label_32.setText("")
#if QT_CONFIG(tooltip)
        self.label_29.setToolTip(QCoreApplication.translate("MainWindow", u"Standard Vehicle", None))
#endif // QT_CONFIG(tooltip)
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Large", None))
        self.label_35.setText("")
#if QT_CONFIG(tooltip)
        self.label_33.setToolTip(QCoreApplication.translate("MainWindow", u"Large Vehicle", None))
#endif // QT_CONFIG(tooltip)
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Cargo Truck", None))
        self.label_23.setText("")
#if QT_CONFIG(tooltip)
        self.label_24.setToolTip(QCoreApplication.translate("MainWindow", u"Truck", None))
#endif // QT_CONFIG(tooltip)
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"E/V", None))
        self.label_26.setText("")
#if QT_CONFIG(tooltip)
        self.label_27.setToolTip(QCoreApplication.translate("MainWindow", u"E/V", None))
#endif // QT_CONFIG(tooltip)
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Fire Alert", None))
#if QT_CONFIG(tooltip)
        self.fireAlertBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Deactivate Fire Alert Button", None))
#endif // QT_CONFIG(tooltip)
        self.fireAlertBtn.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Water Alert", None))
#if QT_CONFIG(tooltip)
        self.waterAlertBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Water Level Alert", None))
#endif // QT_CONFIG(tooltip)
        self.waterAlertBtn.setText("")
        self.smallMonitorLabel.setText(QCoreApplication.translate("MainWindow", u"Input Signal", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"log_id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"deviceStatus", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ino_time", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"position_x", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"position_y", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"direction_x", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"direction_y", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"motorStatus", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"flameStatus", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"waterStatus", None));
        self.refreshTableBtn.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Monitor", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Cam Manual", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"Aim the camera upwards", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Aim the camera downwards", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_5.setToolTip(QCoreApplication.translate("MainWindow", u"Zoom In", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_5.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_4.setToolTip(QCoreApplication.translate("MainWindow", u"Aim the camera to the left", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_4.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(QCoreApplication.translate("MainWindow", u"Aim the camera to the right", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_3.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_8.setToolTip(QCoreApplication.translate("MainWindow", u"Manual Toggle On", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_8.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_7.setToolTip(QCoreApplication.translate("MainWindow", u"Manual Toggle Off", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_7.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_6.setToolTip(QCoreApplication.translate("MainWindow", u"Zoom Out", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_6.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_12.setToolTip(QCoreApplication.translate("MainWindow", u"Manual Moving Stop", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_12.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Moving Stop", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Water toggle", None))
#if QT_CONFIG(tooltip)
        self.pushButton_9.setToolTip(QCoreApplication.translate("MainWindow", u"Water Pump On", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_9.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_10.setToolTip(QCoreApplication.translate("MainWindow", u"Water Pump Off", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_10.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Input signal", None))
#if QT_CONFIG(tooltip)
        self.playBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Play", None))
#endif // QT_CONFIG(tooltip)
        self.playBtn.setText("")
#if QT_CONFIG(tooltip)
        self.pauseBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Pause", None))
#endif // QT_CONFIG(tooltip)
        self.pauseBtn.setText("")
#if QT_CONFIG(tooltip)
        self.stopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Stop", None))
#endif // QT_CONFIG(tooltip)
        self.stopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.zoomInBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Zoom in", None))
#endif // QT_CONFIG(tooltip)
        self.zoomInBtn.setText("")
#if QT_CONFIG(tooltip)
        self.zoomOutBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Zoom out", None))
#endif // QT_CONFIG(tooltip)
        self.zoomOutBtn.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_11.setToolTip(QCoreApplication.translate("MainWindow", u"Open file", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_11.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
#if QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"More...", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Notification Messge", None))
#if QT_CONFIG(tooltip)
        self.closeNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Notification", None))
#endif // QT_CONFIG(tooltip)
        self.closeNotificationBtn.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Copyright by SFR System", None))
#if QT_CONFIG(tooltip)
        self.label_20.setToolTip(QCoreApplication.translate("MainWindow", u"System Operating Status Indicator", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText("")
    # retranslateUi

