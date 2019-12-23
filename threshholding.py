import cv2
#thresholding is avery popular segmentation technique for seperating an object from its background....
# It involves comparing each pixel of image with a predefined threshold value 
img = cv2.imread('gradient.png', 1)

#ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)

cv2.imshow("Image", img)
cv2.imshow("Threshold", th1)
cv2.waitKey(0)
cv2.destroyAllWindows()
