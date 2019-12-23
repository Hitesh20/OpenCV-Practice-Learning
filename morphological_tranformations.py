#  Morphological Image tranformations are some simple operations based on image shape..
# These tranformations are generally performed on binary images
import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('smarties.png', 0)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# it is white square boxes
kernel = np.ones((2,2), np.uint8)
# dilation tranformation
dilation = cv2.dilate(mask, kernel, iterations=2)

erosion = cv2.erode(mask, kernel, iterations=1)

opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)


titles = ['Image', 'Mask', 'Dilation', 'Erosion', 'Opening', 'Closing']
images = [img, mask, dilation, erosion, opening, closing]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()
