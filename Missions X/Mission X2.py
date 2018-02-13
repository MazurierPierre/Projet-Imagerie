import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/Gliese 581d V2.pbm', 0)
des = cv2.medianBlur(img, 3)

kernel = np.ones((2, 2), np.uint8)
opening = cv2.morphologyEx(des, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

# Show
plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(122)
plt.imshow(closing, cmap='gray')
plt.title('Modified'), plt.xticks([]), plt.yticks([])

plt.show()