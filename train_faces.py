import os
from PIL import Image
import numpy as np
import cv2
# to save label id to use in face_recognition_and_identification.py
import pickle


# getting current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# adding images folder to current directory
img_dir = os.path.join(BASE_DIR, "face_images")

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

# recognising starts here
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_ids = {}
x_train = []
y_label = []

for root, dirs, files in os.walk(img_dir):
    for fil in files:
        if fil.endswith("png") or fil.endswith("jpg"):
            path = os.path.join(root, fil)
            label = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower()
            # both are same
            # label = os.path.basename(root).replace(" ", "-").lower()
            #print(label, path)

            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1

            id_ = label_ids[label]
            #print("Label Ids - ", label_ids)

            # training image to numpy array
            pil_image = Image.open(path).convert("L") # coverting into grayScale image
            image_array = np.array(pil_image, "uint8") # converting into  umpy array
            # this is what we want to train on - image_array
            #print(image_array)

            # region of interest in training data
            faces = face_cascade.detectMultiScale(image_array, 1.5, 5)

            for x, y, w, h in faces:
                # these are region of interest
                roi = image_array[y:y+h, x:x+w]
                # we got training data
                x_train.append(roi)
                y_label.append(id_)

                

# print(y_label)
# print(x_train)

with open("labels.pickle", 'wb') as f:
    pickle.dump(label_ids, f)


recognizer.train(x_train, np.array(y_label))
recognizer.save("trainer.yml")