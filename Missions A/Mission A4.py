import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('img/Jupiter1.pbm', 0)
img2 = cv2.imread('img/Jupiter2.pbm', 0)
isize = img1.shape

img = img1

for i in range(0, isize[0]):
    for j in range(0, isize[1]):
        img[i][j] = int(int(img1[i][j]) + int(img2[i][j])) / 2

kernel = np.ones((2, 2), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Image', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()