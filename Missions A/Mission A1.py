import cv2

img = cv2.imread('img/Encelade_surface.pbm', 0)
isize = img.shape
maxi = 0

for i in range(0, isize[0]):
    for j in range(0, isize[1]):
        if img[i][j] > maxi:
            maxi = img[i][j]
            coord = [i, j]

print("Coord", coord, "\nValue", maxi)

cv2.circle(img, (coord[0], coord[1]), 10, (0, 0, 255), 1)

cv2.imshow('img/Encelade_surface.pbm', img)
cv2.waitKey(0)
cv2.destroyAllWindows()