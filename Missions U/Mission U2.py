import cv2
import numpy as np
from matplotlib import pyplot as plt
import imutils

img = cv2.imread('img/U2_surface.pbm', 1)
img_mod = img.copy()

canny = cv2.Canny(img_mod, 500, 300)
cont = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cont = cont[0] if imutils.is_cv2() else cont[1]                                 # Verify if the contour is
cont = sorted(cont, key=cv2.contourArea, reverse=True)[:10]
cv2.drawContours(img_mod, cont, 0, (255, 0, 0), 3)

# Show
plt.subplot(131)
plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(132)
plt.imshow(canny, cmap='gray')
plt.title('Canny'), plt.xticks([]), plt.yticks([])

plt.subplot(133)
plt.imshow(img_mod, cmap='gray')
plt.title('With Contour'), plt.xticks([]), plt.yticks([])

plt.show()
