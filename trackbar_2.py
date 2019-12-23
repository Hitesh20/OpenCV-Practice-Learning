import numpy as np
import cv2


cv2.namedWindow('Image')

def nothing(x):
    print(x)

#create trackbar
cv2.createTrackbar('CP', 'Image', 0, 255, nothing)



switch = 'Color \ Grey'
cv2.createTrackbar(switch, 'Image', 0, 1, nothing)
while(1):
    img = cv2.imread('ronaldo.jpg')
    

    pos =  cv2.getTrackbarPos('CP', 'Image')

    font = cv2.FONT_HERSHEY_DUPLEX
    img = cv2.putText(img, str(pos), (50, 150), font, 2, (0, 0, 155), 5, cv2.LINE_AA)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q') or k == 27:
        break
    

    s = cv2.getTrackbarPos(switch, 'Image')
    if(s == 0):
        pass
    elif(s==1):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.imshow('Image', img)

cv2.destroyAllWindows()