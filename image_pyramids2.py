import cv2
import numpy as np

img = cv2.imread('messi.jpg', 1)
layer = img.copy()

gausian_pyramid = [layer]

for i in range(5):
    layer = cv2.pyrDown(layer)
    gausian_pyramid.append(layer)
    cv2.imshow(str(i), layer)

cv2.imshow('Original_Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()