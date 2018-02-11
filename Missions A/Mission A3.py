import cv2

img = cv2.imread('img/Europa_surface.pbm', 0)
th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11111, 1)

cv2.imshow('img', th)
cv2.waitKey(0)
cv2.destroyAllWindows()