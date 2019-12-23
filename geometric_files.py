import numpy as np
import cv2


#img = cv2.imread('s1.png', 1)

#3args---height, width, 3
#this gives black image
img = np.zeros([512, 512, 3], np.uint8)

img = cv2.line(img, (0,0), (255,255), (255, 0, 0), thickness=10)

img = cv2.arrowedLine(img, (255,0), (255,255), (255, 155, 0), thickness=10)

img = cv2.rectangle(img, (0,255), (400, 400), (0, 255, 255), -1)


font = cv2.FONT_HERSHEY_DUPLEX
img = cv2.putText(img, "Hello", (0, 200), font, 2, (0, 0, 155), 5, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()