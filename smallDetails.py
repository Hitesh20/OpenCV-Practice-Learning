import numpy as np
import cv2

img = cv2.imread('ronaldo.jpg')
img2 = cv2.imread('messi.jpg')
print(img.shape) #returns tuple of number of rows, colums, channels
print(img.size) #returns total no of pixels is accessed
print(img.dtype) #returns image datatype is obtained

b, g, r = cv2.split(img)  #these are bgr channels
img = cv2.merge((b,g,r))

#ROI = region of interest
ball = img[120:40, 170:90]
img[280:40, 330:90] = ball

#merging 2 images- for this the images have to be of same size
dims = (512, 512)
img= cv2.resize(img, dims)
img2 = cv2.resize(img2, dims)
#dst = cv2.add(img, img2)
dst = cv2.addWeighted(img, .7, img2, .3, 3)


cv2.imshow('Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()