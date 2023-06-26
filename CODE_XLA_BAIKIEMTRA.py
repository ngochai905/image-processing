import numpy as np
import imutils
import cv2
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

from imutils.perspective import four_point_transform
from imutils import contours
from PIL import Image,ImageTk

rootscreen =Tk()

def tinhdiem():
    ANSWER_KEY ={0: 1,1: 4,2: 0,3: 3,4: 3}

    image = cv2.imread('Chu Dan Truong-20161185.jpg')
    cv2.imshow("Source", image)
  
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", gray)

    blurred =cv2. GaussianBlur(gray, (5,5), 0)
    cv2.imshow("something", blurred)

    edged = cv2.Canny(blurred, 75, 200)
    cv2.imshow("edged", edged)

    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    docCnt = None

#############################################

    if len(cnts) > 0:
    		
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
		
        for c in cnts:
			
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
			
            if len(approx) == 4:
                docCnt = approx
                break
    
    paper = four_point_transform(image, docCnt.reshape(4,2))
    cv2.imshow("hien ung mat chim cho anh goc", paper)
    warped = four_point_transform(gray, docCnt.reshape(4, 2))
    cv2.imshow("thresh", warped)

    thresh = cv2.threshold(warped, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cv2. imshow("thresh", thresh)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    questionCnts = []
	
    for c in cnts:
		
        (x, y, w, h) = cv2.boundingRect(c)
        ar = w / float(h)
		
        if w >= 20 and h >= 20 and ar >= 0.9 and ar <= 1.1:
            questionCnts.append(c)
	
    questionCnts = contours.sort_contours(questionCnts,method="top-to-bottom")[0]
    correct = 0

    for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)):
		
        cnts = contours.sort_contours(questionCnts[i:i + 5])[0]
        bubbled = None
		
        for (j, c) in enumerate(cnts):
                
            mask = np.zeros(thresh.shape, dtype="uint8")
            cv2.drawContours(mask, [c], -1, 255, -1)
                
            mask = cv2.bitwise_and(thresh, thresh, mask=mask)
            total = cv2.countNonZero(mask)
			
            if bubbled is None or total > bubbled[0]:
                bubbled = (total, j)
				
        color = (0, 0, 255)
        k = ANSWER_KEY[q]
		
        if k == bubbled[1]:
            color = (0, 255, 0)
            correct += 1
		
        cv2.drawContours(paper, [cnts[k]], -1, color, 3)
		
    score = (correct / 5.0) * 100
    cv2.putText(paper, "{:.2f}%".format(score), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    cv2.imshow("exam", paper)
    return

rootscreen.geometry("1286x728+67+0")
rootscreen.title("nhom2_dinh ngochai")
anh=Image.open("Head screen for Image processing.png")
resizeimage = anh.resize((1286,728))
imagebia = ImageTk.PhotoImage(resizeimage)
i1=Label(image=imagebia)
i1.grid(column=0,row=0)

quitButton1 = tk.Button(rootscreen, activebackground="red", text="out screen", font=("time new romen",15), command=rootscreen.quit).place(x=1140, y=680)
contButton1 = tk.Button(rootscreen, activebackground="green", text="continue", font=("time new romen",15), command=lambda:tinhdiem()).place(x=1160, y=635)

rootscreen.mainloop()

cv2.waitKey(0)
cv2.destroyAllWindows

    

        



