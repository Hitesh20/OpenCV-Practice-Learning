import cv2
from matplotlib import pyplot as plt

img = cv2.imread('ronaldo.jpg', -1)
img = cv2.resize(img, (650, 500))
cv2.imshow("Image", img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# to remove x and y axis markings
plt.xticks([]), plt.yticks([])
plt.imshow(img)
plt.show()



cv2.waitKey(0)
cv2.destroyAllWindows()