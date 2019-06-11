import cv2
import numpy as np 

img1 = cv2.imread("./image/highway_001.jpg")
gray = cv2.cvtColor(img1,cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray,(5,5), 0)
canny = cv2.Canny(blur,50,100)
cv2.imshow("Blur",blur)
cv2.imshow("Result",canny)
cv2.waitKey()
cv2.destroyAllWindows()