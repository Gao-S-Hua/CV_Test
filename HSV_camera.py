import cv2
import numpy as np 
import imutils
cap = cv2.VideoCapture(0)
lower_hsv = np.array([0,100,100])
upper_hsv = np.array([255,255,200])

while True :
    rtn, frame = cap.read()
    frame = imutils.resize(frame, width=640, height=360)
    HSV_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow("Camera_HSV",HSV_frame)
    mask = cv2.inRange(HSV_frame,lower_hsv,upper_hsv)
    res = cv2.bitwise_and(frame,frame,mask = mask)
    cv2.imshow("Camera",res)
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break


# H > 100
# S > 100