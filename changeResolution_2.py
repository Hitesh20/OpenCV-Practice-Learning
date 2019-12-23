import numpy as np
import cv2
import datetime

cap = cv2.VideoCapture(0)



def make_1080p():
    #for width 
    cap.set(3, 1920)
    #for height 
    cap.set(4, 1080)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)


make_1080p()
while cap.isOpened():

    ret, frame = cap.read()

    frame = cv2.putText(frame, str(datetime.datetime.now()), (2, 50), cv2.FONT_HERSHEY_PLAIN, 4, (0,255,255), 2)

    cv2.imshow('frame', frame)

     #so that when we press q windows get closed
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()