from imutils.perspective import four_point_transform
from imutils import contours

import numpy as np
import imutils
import cv2

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (
    QCoreApplication,
    QPropertyAnimation,
    QDate,
    QDateTime,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
    QEvent,
)
from PyQt5.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QKeySequence,
    QLinearGradient,
    QPalette,
    QPainter,
    QPixmap,
    QRadialGradient,
)
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QColor,QImage
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt,QObject

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.storeimg =''
        self.answer1  =''
        self.answer2  =''
        self.answer3  =''
        self.answer4  =''
        self.answer5  =''

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        # resolve
        self.ui.Btn_chamdiem.clicked.connect(self.hamcon)
        self.ui.send_img.clicked.connect(self.send_image)

        # btn Quit
        self.ui.Btn_Quit.clicked.connect(QtCore.QCoreApplication.quit)
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    def send_image(self):
        self.fileName = QFileDialog.getOpenFileName(self,'Image Files(*.png *.jpg *.bmp)')
        if self.fileName:
            self.ui.source.setPixmap(QtGui.QPixmap(str(self.fileName[0])))
            # print(self.fileName[0])
            self.ui.source.setScaledContents(True)
            self.storeimg = self.fileName[0]

        
    def hamcon(self):
        if (
            self.ui.answer1 != "Answer"
            and self.ui.answer2 != "Answer"
            and self.ui.answer3 != "Answer"
            and self.ui.answer4 != "Answer"
            and self.ui.answer5 != "Answer"
        ):
            self.answer1 = self.ui.answer1.currentText()
            self.answer2 = self.ui.answer2.currentText()
            self.answer3 = self.ui.answer3.currentText()
            self.answer4 = self.ui.answer4.currentText()
            self.answer5 = self.ui.answer5.currentText()
            ####################### answer 1
            if(self.answer1 == 'A'):
                self.answer1 = 0
            if(self.answer1 == 'B'):
                self.answer1 =1
            if(self.answer1 == 'C'):
                self.answer1 = 2
            if(self.answer1 == 'D'):
                self.answer1 =3
            if(self.answer1 == 'E'):
                self.answer1 = 4
            ######################## answer 2        
            if(self.answer2 == 'A'):
                self.answer2 = 0
            if(self.answer2 == 'B'):
                self.answer2 =1
            if(self.answer2 == 'C'):
                self.answer2 = 2
            if(self.answer2 == 'D'):
                self.answer2 =3
            if(self.answer2 == 'E'):
                self.answer2 = 4 
            ######################## answer 3  
            if(self.answer3 == 'A'):
                self.answer3 = 0
            if(self.answer3 == 'B'):
                self.answer3 =1
            if(self.answer3 == 'C'):
                self.answer3 = 2
            if(self.answer3 == 'D'):
                self.answer3 =3
            if(self.answer3 == 'E'):
                self.answer3 = 4  
            ######################## answer 4  
            if(self.answer4 == 'A'):
                self.answer4 = 0
            if(self.answer4 == 'B'):
                self.answer4 =1
            if(self.answer4 == 'C'):
                self.answer4 = 2
            if(self.answer4 == 'D'):
                self.answer4 =3
            if(self.answer4 == 'E'):
                self.answer4 = 4 
                ######################## answer 5  
            if(self.answer5 == 'A'):
                self.answer5 = 0
            if(self.answer5 == 'B'):
                self.answer5 =1
            if(self.answer5 == 'C'):
                self.answer5 = 2
            if(self.answer5 == 'D'):
                self.answer5 =3
            if(self.answer5 == 'E'):
                self.answer5 = 4       


        ANSWER_KEY = {0: int(self.answer1), 1: int(self.answer2), 2: int(self.answer3), 3: int(self.answer4), 4: int(self.answer5)}
        self.image = cv2.imread(str(self.storeimg),cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(blurred, 75, 200)
        
        cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        docCnt = None

        if len(cnts) > 0:
    		
            cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
		
        for c in cnts:
			
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
			
            if len(approx) == 4:
                docCnt = approx
                break

        self.paper = four_point_transform(self.image, docCnt.reshape(4, 2))   

        warped = four_point_transform(gray, docCnt.reshape(4, 2))

        self.thresh = cv2.threshold(warped, 0, 255,
		    cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

        self.img_thresh = cv2.cvtColor(self.thresh.copy(), cv2.COLOR_GRAY2BGR)
	
		
        cnts = cv2.findContours(self.thresh.copy(), cv2.RETR_EXTERNAL,
		    cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        questionCnts = []
	
        for c in cnts:
		
            (x, y, w, h) = cv2.boundingRect(c)
            ar = w / float(h)
		
            if w >= 20 and h >= 20 and ar >= 0.9 and ar <= 1.1:
                questionCnts.append(c)
	
        questionCnts = contours.sort_contours(questionCnts,
		    method="top-to-bottom")[0]
        correct = 0
	#########################################
	
        for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)):
		
            cnts = contours.sort_contours(questionCnts[i:i + 5])[0]
            bubbled = None
		
            for (j, c) in enumerate(cnts):
                
                mask = np.zeros(self.thresh.shape, dtype="uint8")
                cv2.drawContours(mask, [c], -1, 255, -1)
                
                mask = cv2.bitwise_and(self.thresh, self.thresh, mask=mask)
                total = cv2.countNonZero(mask)
			
                if bubbled is None or total > bubbled[0]:
                    bubbled = (total, j)
				
            color = (0, 0, 255)
            k = ANSWER_KEY[q]
		
            if k == bubbled[1]:
                color = (0, 255, 0)
                correct += 1
		
            cv2.drawContours(self.paper, [cnts[k]], -1, color, 3)
		
        score = (correct / 5.0) * 100
        print("[INFO] score: {:.2f}%".format(score))
        cv2.putText(self.paper, "{:.2f}%".format(score), (10, 30),
		    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        
        # cv2.imshow("thress", thresh)
        # cv2.imshow("Exam", self.paper)

        # self.image = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0], self.image.shape[1]*self.image.shape[2] , QtGui.QImage.Format_RGB888).rgbSwapped()
        # self.ui.source.setPixmap(QtGui.QPixmap.fromImage(self.image))
        # self.ui.source.setScaledContents(True)

        # self.qImg = QtGui.QImage(self.img_thresh.data, self.img_thresh.shape[1], self.img_thresh.shape[0], self.img_thresh.shape[2]*self.img_thresh.shape[1],QtGui.QImage.Format_RGB888)
        # self.ui.thresh.setPixmap(QtGui.QPixmap.fromImage(self.qImg))
        # self.ui.thresh.setScaledContents(True)


        self.qImgpaper = QtGui.QImage(self.paper.data, self.paper.shape[1], self.paper.shape[0], self.paper.shape[1]*self.paper.shape[2] ,QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.paper.setPixmap(QtGui.QPixmap.fromImage(self.qImgpaper))
        self.ui.paper.setScaledContents(True)


        point = (correct / 5.0) * 10
        self.ui.result.setText(str(np.round(point, 1)))
        
        x = self.storeimg.split("/")

        y = x[len(x)-1]

        z = y.split(".")

        k = z[0]
        self.l = k.split("-")
        
        self.ui.Name_out.setText(self.l[0])
        self.ui.code.setText(self.l[1])

        







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
