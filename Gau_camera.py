import cv2
import numpy as np 
import imutils
cap = cv2.VideoCapture(0)

while True :
    rtn, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5), 0)
    canny = cv2.Canny(blur,30,150)
    cv2.imshow("Canny",canny)


    if cv2.waitKey(1) & 0xFF == ord('q') :
        break