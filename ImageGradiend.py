## Image Gradient is the directional change in the intensity or color in Image


#  Morphological Image tranformations are some simple operations based on image shape..
# These tranformations are generally performed on binary images
import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('messi.jpg', 0)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize = 3)
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX))

sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))

sobelXY = cv2.Sobel(img, cv2.CV_64F, 1, 1)
sobelXY = np.uint8(np.absolute(sobelXY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ['Gray Messi', 'Laplasian', 'sobelX', 'sobelY', 'SobelXY', 'Sobel Combined']
images = [img, lap, sobelX, sobelY, sobelXY, sobelCombined]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()
