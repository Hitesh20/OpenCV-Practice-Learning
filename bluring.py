#  Morphological Image tranformations are some simple operations based on image shape..
# These tranformations are generally performed on binary images
import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('opencv-logo.png', 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernel = np.ones((5, 5), np.float32)/25


dst = cv2.filter2D(img, -1, kernel)
# LPF - low pass filter - helps in removing noises and bluring the image
blur = cv2.blur(img, (5, 5))
gausian_blur = cv2.GaussianBlur(img, (5, 5), 0)

##similarry we have median blur which takes median of itself and next pixel and then show results
## we also have bilateralFilter which blur image and preserves the edges


# HPF = High pass filter - helps in finding edges in the image

titles = ['Image', '2D Filter', 'Blur', 'Gausian Blur']
images = [img, dst, blur, gausian_blur]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()
