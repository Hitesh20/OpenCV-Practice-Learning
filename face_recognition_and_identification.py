import cv2
import numpy as np

#classifier- this classifier works with gray scale images
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)
while cap.isOpened():
    # capturing frame by frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for x, y, w, h in faces:
        # these are region of interest
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # recognise? - deep learned program model to predict things.. 


        '''
        img_item = "my_img.png"
        # saves the portion of image
        cv2.imwrite(img_item, roi_gray)
        '''
        # drawing rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 3)

    

    # Display resulting frame
    cv2.imshow('Video', frame)

    # press q to break
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

# camera got released when everything ends
cap.release()
# it destroys all windows at the end
cv2.destroyAllWindows()