# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1878, 1011)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMinimumSize(QSize(0, 60))
        self.Top_Bar.setMaximumSize(QSize(16777215, 60))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setGeometry(QRect(0, 0, 68, 60))
        self.frame_toggle.setMinimumSize(QSize(68, 60))
        self.frame_toggle.setMaximumSize(QSize(68, 60))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        self.Btn_Toggle.setGeometry(QRect(0, 0, 68, 60))
        self.Btn_Toggle.setMinimumSize(QSize(68, 60))
        self.Btn_Toggle.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.label_2 = QLabel(self.Top_Bar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 0, 1791, 60))
        self.label_2.setMinimumSize(QSize(1791, 60))
        self.label_2.setMaximumSize(QSize(1791, 60))
        font = QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0, 60))
        self.btn_page_1.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/16x16/icons/16x16/cil-home.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:  rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.btn_page_1)

        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 60))
        font1 = QFont()
        font1.setFamily(u"MS Reference Sans Serif")
        self.btn_page_2.setFont(font1)
        self.btn_page_2.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/16x16/icons/16x16/cil-screen-desktop.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:  rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.btn_page_2)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)

        self.Btn_Quit = QPushButton(self.frame_left_menu)
        self.Btn_Quit.setObjectName(u"Btn_Quit")
        self.Btn_Quit.setMinimumSize(QSize(0, 60))
        self.Btn_Quit.setMaximumSize(QSize(16777215, 60))
        self.Btn_Quit.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/16x16/icons/16x16/cil-power-standby.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:  rgb(255, 0, 0);\n"
"	border-left: 28px solid rgb(255, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.Btn_Quit)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_1 = QLabel(self.page_1)
        self.label_1.setObjectName(u"label_1")
        font2 = QFont()
        font2.setPointSize(40)
        self.label_1.setFont(font2)
        self.label_1.setStyleSheet(u"color: #FFF;")
        self.label_1.setPixmap(QPixmap(u"Head screen for Image processing.png"))
        self.label_1.setScaledContents(True)
        self.label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.layoutWidget = QWidget(self.page_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(330, 70, 1450, 780))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setSpacing(30)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.source = QLabel(self.layoutWidget)
        self.source.setObjectName(u"source")
        self.source.setMinimumSize(QSize(700, 700))
        self.source.setMaximumSize(QSize(700, 700))
        font3 = QFont()
        font3.setPointSize(12)
        self.source.setFont(font3)
        self.source.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.source.setScaledContents(True)
        self.source.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.source, 0, 0, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 30))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(100, 30))
        font4 = QFont()
        font4.setFamily(u"MS Shell Dlg 2")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setWeight(50)
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 1, 1, 1, 1)

        self.paper = QLabel(self.layoutWidget)
        self.paper.setObjectName(u"paper")
        self.paper.setMinimumSize(QSize(700, 700))
        self.paper.setMaximumSize(QSize(700, 700))
        self.paper.setFont(font3)
        self.paper.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.paper.setScaledContents(True)
        self.paper.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.paper, 0, 1, 1, 1)

        self.layoutWidget1 = QWidget(self.page_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(-10, 380, 342, 91))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.send_img = QPushButton(self.layoutWidget1)
        self.send_img.setObjectName(u"send_img")
        self.send_img.setMinimumSize(QSize(156, 50))
        self.send_img.setMaximumSize(QSize(180, 50))
        self.send_img.setFont(font3)
        self.send_img.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 255, 255);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.send_img)

        self.Btn_chamdiem = QPushButton(self.layoutWidget1)
        self.Btn_chamdiem.setObjectName(u"Btn_chamdiem")
        self.Btn_chamdiem.setMinimumSize(QSize(156, 50))
        self.Btn_chamdiem.setMaximumSize(QSize(180, 50))
        self.Btn_chamdiem.setFont(font3)
        self.Btn_chamdiem.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 255, 255);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.Btn_chamdiem)

        self.layoutWidget2 = QWidget(self.page_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 540, 331, 201))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget2)
        self.label_11.setObjectName(u"label_11")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(45, 45, 45, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.label_11.setPalette(palette)
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_11.setFont(font5)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.label_11)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.Name_out = QLineEdit(self.layoutWidget2)
        self.Name_out.setObjectName(u"Name_out")
        self.Name_out.setMinimumSize(QSize(30, 30))
        palette1 = QPalette()
        brush5 = QBrush(QColor(27, 29, 35, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush5)
        brush6 = QBrush(QColor(255, 255, 255, 128))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        brush7 = QBrush(QColor(120, 120, 120, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        brush8 = QBrush(QColor(0, 0, 0, 128))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.Name_out.setPalette(palette1)
        self.Name_out.setFont(font3)
        self.Name_out.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.Name_out, 0, 1, 1, 1)

        self.result = QLineEdit(self.layoutWidget2)
        self.result.setObjectName(u"result")
        self.result.setMinimumSize(QSize(30, 30))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.result.setPalette(palette2)
        self.result.setFont(font3)
        self.result.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.result, 2, 1, 1, 1)

        self.label_10 = QLabel(self.layoutWidget2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(70, 30))
        self.label_10.setMaximumSize(QSize(70, 30))
        self.label_10.setFont(font3)
        self.label_10.setMouseTracking(False)
        self.label_10.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)

        self.label_9 = QLabel(self.layoutWidget2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(70, 30))
        self.label_9.setMaximumSize(QSize(70, 30))
        self.label_9.setFont(font3)
        self.label_9.setMouseTracking(False)
        self.label_9.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_12 = QLabel(self.layoutWidget2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(70, 30))
        self.label_12.setMaximumSize(QSize(70, 30))
        self.label_12.setFont(font3)
        self.label_12.setMouseTracking(False)
        self.label_12.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)

        self.code = QLineEdit(self.layoutWidget2)
        self.code.setObjectName(u"code")
        self.code.setMinimumSize(QSize(30, 30))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.code.setPalette(palette3)
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setWeight(50)
        self.code.setFont(font6)
        self.code.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.code, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)

        self.layoutWidget3 = QWidget(self.page_2)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(0, 68, 193, 311))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_8.setSpacing(7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.layoutWidget3)
        self.label_18.setObjectName(u"label_18")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush9 = QBrush(QColor(255, 255, 255, 128))
        brush9.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush10 = QBrush(QColor(255, 255, 255, 128))
        brush10.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush11 = QBrush(QColor(255, 255, 255, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.label_18.setPalette(palette4)
        self.label_18.setFont(font5)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.label_18)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_13 = QLabel(self.layoutWidget3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(70, 30))
        self.label_13.setMaximumSize(QSize(70, 30))
        self.label_13.setFont(font3)
        self.label_13.setMouseTracking(False)
        self.label_13.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_13)

        self.answer1 = QComboBox(self.layoutWidget3)
        self.answer1.addItem("")
        self.answer1.addItem("")
        self.answer1.addItem("")
        self.answer1.addItem("")
        self.answer1.addItem("")
        self.answer1.addItem("")
        self.answer1.setObjectName(u"answer1")
        self.answer1.setMinimumSize(QSize(110, 40))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(10)
        self.answer1.setFont(font7)
        self.answer1.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);	\n"
"	background-color: rgb(52, 59, 72);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(52, 59, 72);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }")

        self.horizontalLayout.addWidget(self.answer1)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_14 = QLabel(self.layoutWidget3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(70, 30))
        self.label_14.setMaximumSize(QSize(70, 30))
        self.label_14.setFont(font3)
        self.label_14.setMouseTracking(False)
        self.label_14.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_14)

        self.answer2 = QComboBox(self.layoutWidget3)
        self.answer2.addItem("")
        self.answer2.addItem("")
        self.answer2.addItem("")
        self.answer2.addItem("")
        self.answer2.addItem("")
        self.answer2.addItem("")
        self.answer2.setObjectName(u"answer2")
        self.answer2.setMinimumSize(QSize(110, 40))
        self.answer2.setFont(font7)
        self.answer2.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);	\n"
"	background-color: rgb(52, 59, 72);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(52, 59, 72);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }")

        self.horizontalLayout_4.addWidget(self.answer2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_15 = QLabel(self.layoutWidget3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(70, 30))
        self.label_15.setMaximumSize(QSize(70, 30))
        self.label_15.setFont(font3)
        self.label_15.setMouseTracking(False)
        self.label_15.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_15)

        self.answer3 = QComboBox(self.layoutWidget3)
        self.answer3.addItem("")
        self.answer3.addItem("")
        self.answer3.addItem("")
        self.answer3.addItem("")
        self.answer3.addItem("")
        self.answer3.addItem("")
        self.answer3.setObjectName(u"answer3")
        self.answer3.setMinimumSize(QSize(110, 40))
        self.answer3.setFont(font7)
        self.answer3.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);	\n"
"	background-color: rgb(52, 59, 72);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(52, 59, 72);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }")

        self.horizontalLayout_5.addWidget(self.answer3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_16 = QLabel(self.layoutWidget3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(70, 30))
        self.label_16.setMaximumSize(QSize(70, 30))
        self.label_16.setFont(font3)
        self.label_16.setMouseTracking(False)
        self.label_16.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_16)

        self.answer4 = QComboBox(self.layoutWidget3)
        self.answer4.addItem("")
        self.answer4.addItem("")
        self.answer4.addItem("")
        self.answer4.addItem("")
        self.answer4.addItem("")
        self.answer4.addItem("")
        self.answer4.setObjectName(u"answer4")
        self.answer4.setMinimumSize(QSize(110, 40))
        self.answer4.setFont(font7)
        self.answer4.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);	\n"
"	background-color: rgb(52, 59, 72);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(52, 59, 72);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }")

        self.horizontalLayout_6.addWidget(self.answer4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_17 = QLabel(self.layoutWidget3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(70, 30))
        self.label_17.setMaximumSize(QSize(70, 30))
        self.label_17.setFont(font3)
        self.label_17.setMouseTracking(False)
        self.label_17.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_17)

        self.answer5 = QComboBox(self.layoutWidget3)
        self.answer5.addItem("")
        self.answer5.addItem("")
        self.answer5.addItem("")
        self.answer5.addItem("")
        self.answer5.addItem("")
        self.answer5.addItem("")
        self.answer5.setObjectName(u"answer5")
        self.answer5.setMinimumSize(QSize(110, 40))
        self.answer5.setFont(font7)
        self.answer5.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);	\n"
"	background-color: rgb(52, 59, 72);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(52, 59, 72);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }")

        self.horizontalLayout_7.addWidget(self.answer5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Giao di\u1ec7n ch\u1ea5m \u0111i\u1ec3m thi tr\u1eafc nghi\u1ec7m - Tr\u01b0\u1eddng X ", None))
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"GUI", None))
        self.Btn_Quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.label_1.setText("")
        self.source.setText(QCoreApplication.translate("MainWindow", u"H\u00ecnh ch\u1ee5p t\u1eeb sinh vi\u00ean", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"H\u00ecnh ch\u1ee5p t\u1eeb sinh vi\u00ean", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"K\u1ebft qu\u1ea3 ", None))
        self.paper.setText(QCoreApplication.translate("MainWindow", u"K\u1ebft qu\u1ea3 ", None))
        self.send_img.setText(QCoreApplication.translate("MainWindow", u"T\u1ea3i h\u00ecnh l\u00ean", None))
        self.Btn_chamdiem.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ea5m \u0111i\u1ec3m", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"K\u1ebft qu\u1ea3", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0110i\u1ec3m", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"T\u00ean", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"MSSV", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp \u0111\u00e1p \u00e1n", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"C\u00e2u 1", None))
        self.answer1.setItemText(0, QCoreApplication.translate("MainWindow", u"Answer", None))
        self.answer1.setItemText(1, QCoreApplication.translate("MainWindow", u"A", None))
        self.answer1.setItemText(2, QCoreApplication.translate("MainWindow", u"B", None))
        self.answer1.setItemText(3, QCoreApplication.translate("MainWindow", u"C", None))
        self.answer1.setItemText(4, QCoreApplication.translate("MainWindow", u"D", None))
        self.answer1.setItemText(5, QCoreApplication.translate("MainWindow", u"E", None))

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"C\u00e2u 2", None))
        self.answer2.setItemText(0, QCoreApplication.translate("MainWindow", u"Answer", None))
        self.answer2.setItemText(1, QCoreApplication.translate("MainWindow", u"A", None))
        self.answer2.setItemText(2, QCoreApplication.translate("MainWindow", u"B", None))
        self.answer2.setItemText(3, QCoreApplication.translate("MainWindow", u"C", None))
        self.answer2.setItemText(4, QCoreApplication.translate("MainWindow", u"D", None))
        self.answer2.setItemText(5, QCoreApplication.translate("MainWindow", u"E", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"C\u00e2u 3", None))
        self.answer3.setItemText(0, QCoreApplication.translate("MainWindow", u"Answer", None))
        self.answer3.setItemText(1, QCoreApplication.translate("MainWindow", u"A", None))
        self.answer3.setItemText(2, QCoreApplication.translate("MainWindow", u"B", None))
        self.answer3.setItemText(3, QCoreApplication.translate("MainWindow", u"C", None))
        self.answer3.setItemText(4, QCoreApplication.translate("MainWindow", u"D", None))
        self.answer3.setItemText(5, QCoreApplication.translate("MainWindow", u"E", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"C\u00e2u 4", None))
        self.answer4.setItemText(0, QCoreApplication.translate("MainWindow", u"Answer", None))
        self.answer4.setItemText(1, QCoreApplication.translate("MainWindow", u"A", None))
        self.answer4.setItemText(2, QCoreApplication.translate("MainWindow", u"B", None))
        self.answer4.setItemText(3, QCoreApplication.translate("MainWindow", u"C", None))
        self.answer4.setItemText(4, QCoreApplication.translate("MainWindow", u"D", None))
        self.answer4.setItemText(5, QCoreApplication.translate("MainWindow", u"E", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"C\u00e2u 5", None))
        self.answer5.setItemText(0, QCoreApplication.translate("MainWindow", u"Answer", None))
        self.answer5.setItemText(1, QCoreApplication.translate("MainWindow", u"A", None))
        self.answer5.setItemText(2, QCoreApplication.translate("MainWindow", u"B", None))
        self.answer5.setItemText(3, QCoreApplication.translate("MainWindow", u"C", None))
        self.answer5.setItemText(4, QCoreApplication.translate("MainWindow", u"D", None))
        self.answer5.setItemText(5, QCoreApplication.translate("MainWindow", u"E", None))

    # retranslateUi

