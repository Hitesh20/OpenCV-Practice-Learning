## It is an edge detection operator that uses a multistage algorithm to detect a wide range of edges in images.


#  Morphological Image tranformations are some simple operations based on image shape..
# These tranformations are generally performed on binary images
import cv2
from matplotlib import pyplot as plt
import numpy as np


def nothing(x):
    pass

cv2.namedWindow('Tracker')
cv2.createTrackbar('Threshold1', 'Tracker', 0, 255, nothing)
cv2.createTrackbar('Threshold2', 'Tracker', 0, 255, nothing)

while True:

    img = cv2.imread('messi.jpg', 0)

    trackbar_position1 = cv2.getTrackbarPos('Threshold1', 'Tracker')
    trackbar_position2 = cv2.getTrackbarPos('Threshold2', 'Tracker')

    canny = cv2.Canny(img, trackbar_position1, trackbar_position2)
    

    cv2.imshow('Original Image', img)
        
    cv2.imshow('Canny Image', canny)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()