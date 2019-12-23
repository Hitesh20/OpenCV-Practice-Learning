import numpy as np
import cv2

img = np.zeros([300, 512, 3], np.uint8)
cv2.namedWindow('Image')

def nothing(x):
    print(x)

#create trackbar
cv2.createTrackbar('B', 'Image', 0, 255, nothing)
cv2.createTrackbar('G', 'Image', 0, 255, nothing)
cv2.createTrackbar('R', 'Image', 0, 255, nothing)

switch = '0 : off \n 1 : on'
cv2.createTrackbar(switch, 'Image', 0, 1, nothing)
while(1):
    cv2.imshow('Image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q') or k == 27:
        break
    b = cv2.getTrackbarPos('B', 'Image')
    g = cv2.getTrackbarPos('G', 'Image')
    r = cv2.getTrackbarPos('R', 'Image')

    s = cv2.getTrackbarPos(switch, 'Image')
    if(s == 0):
        img[:] = 0
    elif(s==1):
        img[:] = [b, g, r] 

cv2.destroyAllWindows()