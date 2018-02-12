import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img/Gliese 667Cc_surface.pbm', 0)


def showPlot(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show()


#cv2.imshow('img/Encelade_surface.pbm', img)
#img = cv2.imread('img/Gliese 667Cc_surface.pbm', 0)
#cv2.normalize(img, img, 255, 255, 1)  # Normalize
img = cv2.equalizeHist(img)  # Equalize
cv2.imshow('Modified Image', img)

showPlot(img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.destroyAllWindows()
