import cv2
import numpy as np

img = cv2.imread('opencv-logo.png', 1)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, herarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print("No of contours " + str(len(contours)))

cv2.drawContours(img, contours, -1, (10, 215, 80), 3)

cv2.imshow('Original_Image', img)
cv2.imshow('Gray_Image', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()