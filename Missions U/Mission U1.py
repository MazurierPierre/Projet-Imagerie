import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/U1_surface.pbm', 0)

# Laplacian
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# Sobel
sobel = cv2.Sobel(img, cv2.CV_8U, 1, 1, 3)

# Canny
canny = cv2.Canny(img, 100, 200)

# Show
plt.subplot(141)
plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(142)
plt.imshow(sobel, cmap='gray')
plt.title('Sobel'), plt.xticks([]), plt.yticks([])

plt.subplot(143)
plt.imshow(canny, cmap='gray')
plt.title('Canny'), plt.xticks([]), plt.yticks([])

plt.subplot(144)
plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

plt.show()
