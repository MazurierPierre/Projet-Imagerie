import cv2

img = cv2.imread('img/Mars_surface.pbm', 0)
isize = img.shape
value = 0

for i in range(0, isize[0]):
    for j in range(0, isize[1]):
        value += img[i][j]

print((value / ( (i + 1) * (j + 1) )) * 100 / 255)

cv2.imshow('img/Encelade_surface.pbm', img)
cv2.waitKey(0)
cv2.destroyAllWindows()