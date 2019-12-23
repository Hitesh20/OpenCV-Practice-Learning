import cv2

img = cv2.imread('sudoku.jpeg', 0)

#_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow("Image", img)
cv2.imshow("Threshold", th1)
cv2.waitKey(0)
cv2.destroyAllWindows()