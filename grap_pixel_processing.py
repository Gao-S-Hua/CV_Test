import cv2
import numpy as np 

img1 = cv2.imread("./image/a.png",cv2.IMREAD_COLOR)
rows, cols, chals = img1.shape
print(rows,cols,chals)
img1_gray = cv2.cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#cv2.imshow('img1',img1)
cv2.imshow('img1_gray',img1_gray)

blank_image_avg = np.zeros((rows,cols,1), np.uint8)
blank_image_wavg = np.zeros((rows,cols,1), np.uint8)

for i in range(0,rows-1) :
    for j in range(0, cols-1) :
        blank_image_avg[i,j] = sum(img1[i,j])/3
for i in range(0,rows-1) :
    for j in range(0, cols-1) :
        blank_image_wavg[i,j] = img1[i,j][0] * 0.3 + img1[i,j][1] * 0.59 + img1[i,j][2] * 0.11
cv2.imshow('My_AVG_grap', blank_image_avg)
cv2.imshow('My_WAVG_grap', blank_image_wavg)
cv2.waitKey()
cv2.destroyAllWindows()