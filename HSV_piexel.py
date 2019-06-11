import cv2
import numpy as np 

#img1 = cv2.imread("./image/a.png",cv2.IMREAD_COLOR)
img1 = cv2.imread("./image/HSL_HSV_2.png",cv2.IMREAD_COLOR)

rows, cols, chals = img1.shape
print(rows,cols,chals)
img1_hsv = cv2.cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV_img', img1_hsv)
cv2.imshow('RGB', img1)
cv2.waitKey()
cv2.destroyAllWindows()
