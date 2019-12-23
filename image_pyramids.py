import cv2
import numpy as np

img = cv2.imread('messi.jpg', 1)

lower_resolution = cv2.pyrDown(img)
increase_resolution = cv2.pyrUp(img)

cv2.imshow('Original_Image', img)
cv2.imshow('Reduced Resolution', lower_resolution)
cv2.imshow('Increased Resolution', increase_resolution)
cv2.waitKey(0)
cv2.destroyAllWindows()