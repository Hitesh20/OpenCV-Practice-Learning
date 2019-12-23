## It is an edge detection operator that uses a multistage algorithm to detect a wide range of edges in images.


#  Morphological Image tranformations are some simple operations based on image shape..
# These tranformations are generally performed on binary images
import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('messi.jpg', 0)

canny = cv2.Canny(img, 100, 200)

titles = ['Image', 'Canny']
images = [img, canny]

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()
