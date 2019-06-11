import cv2
import numpy as np 

img1 = cv2.imread("./image/a.png",cv2.IMREAD_COLOR)

rows, cols, chals = img1.shape
print(img1[100,400])
img1_hsv = cv2.cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)



blank_image = np.zeros((rows,cols,3), np.uint8)
for i in range(0,rows-1) :
    for j in range(0, cols-1) :
        MAX = int(max(img1[i,j]))
        MIN = int(min(img1[i,j]))
        v = MAX
        if(MAX == 0) :
            s = 0
        else :
            s = 1 - float(MIN/MAX)
        R = int(img1[i,j][2])
        G = int(img1[i,j][1])
        B = int(img1[i,j][0])
        if( MAX == MIN) :
            h = 0
        elif(MAX == R) and (G >= B) :
            h = 60.0 * (G - B) / (MAX - MIN)
        elif (MAX == R and G < B) :
            h = 60.0 * (G - B) / (MAX - MIN)+ 360
        elif MAX == G :
            h = 60.0 * (B - R) / (MAX - MIN) + 120
        elif (MAX == B) :
            h = 60.0 * (R - G)/ (MAX - MIN) + 240
        #v = int(v * 255)
        #s = int(s * 255)
        #h = int(h / 2)
        #blank_image[i,j] = [l, s, h]
        v = np.uint8(v)
        s = np.uint8(int(s*255))
        h = np.uint8( int(h/2))
        blank_image[i,j] = [h,s,v]

cv2.imshow('HSV_img', img1_hsv)
cv2.imshow('RGB', img1)
cv2.imshow('my_HSV', blank_image)
cv2.waitKey()
cv2.destroyAllWindows()