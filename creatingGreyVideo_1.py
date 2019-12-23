import numpy as np
import cv2

#we need Capture device
capture = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = capture.read()


    #cvtColor means convert Color   #upar vale frame ka color change kia h.....
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ##Displaying only.... 1 argument is window name and 2 is actual frames that we see
    cv2.imshow('frame', frame)
    cv2.imshow('gray frame', gray)

    #so that when we press q windows get closed
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
capture.release()
cv2.destroyAllWindows()