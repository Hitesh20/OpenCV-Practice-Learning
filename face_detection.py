import cv2
import numpy as np

#classifier- this classifier works with gray scale images
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#img = cv2.imread('messi.jpg')
cap = cv2.VideoCapture(0)
while cap.isOpened():
    _, img = cap.read()

    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # faces vector - contains all the faces in video or picture
    faces = face_cascade.detectMultiScale(imgray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)

    cv2.imshow('Image', img)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()