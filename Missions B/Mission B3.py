import cv2
from matplotlib import pyplot as plt

COLOR1 = [0, 0, 0]
COLOR2 = [255, 64, 0]
COLOR3 = [0, 64, 255]
COLOR4 = [255, 255, 255]

img = cv2.imread('img/HD215497.pbm', 1)
isize = img.shape

avg = 0
all = 0

for i in range(0, isize[0]):
    for j in range(0, isize[1]):
        all += img[i][j][0]

avg = all / (i * j)

i = j = 0
for i in range(0, isize[0]):
    for j in range(0, isize[1]):
        if img[i][j][0] < (avg / 2):
            img[i][j] = COLOR1
        if img[i][j][0] > (avg * 2):
            img[i][j] = COLOR4
        if img[i][j][0] < avg and img[i][j][0] >= (avg / 2):
            img[i][j] = COLOR2
        if img[i][j][0] > avg and img[i][j][0] <= (avg * 2):
            img[i][j] = COLOR3

# Show
cv2.imshow('Modified Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.destroyAllWindows()
