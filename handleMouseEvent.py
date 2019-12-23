import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)


#these are nessecary arguments
def clickEvent(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(img, str(x) + ' ' + str(y), (x, y), font, 1, (78, 123, 155), 2, cv2.LINE_AA)
        cv2.imshow('Image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x ,1]
        red = img[y, x, 2]
        print(blue, green, red)
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(img, str(blue) + ' ' + str(green) + ' ' + str(red), (x, y), font, 1, (179, 23, 55), 1, cv2.LINE_AA)
        cv2.imshow('Image', img)


# img = np.zeros([700, 650, 3], np.uint8)
img = cv2.imread('s2.png')
cv2.imshow('Image', img)


#this function is used to call the call back function i.e. clickEvent
#1 argument - window name and 2 argument - event that we created
cv2.setMouseCallback('Image', clickEvent)

cv2.waitKey(0)

cv2.destroyAllWindows()