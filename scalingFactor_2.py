import numpy as np
import cv2


cap = cv2.VideoCapture(0)

def rescaleFrame(frame, percent=75):

    ## height, width, channel = frame.shape   ------these 3 that we ger from frame.shape
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

while True:

    ret, frame = cap.read()
    

    #resizing frame by calling function that we created above
    frame = rescaleFrame(frame, 45)


    cv2.imshow('frame', frame)




     #so that when we press q windows get closed
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()