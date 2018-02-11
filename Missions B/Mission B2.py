import cv2
from matplotlib import pyplot as plt


def showPlot(image):
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()


img = cv2.imread('img/GD61.pbm', 0)

# Treatment
cv2.normalize(img, img, 255, 255, 1)  # Normalize
mod = cv2.fastNlMeansDenoising(img, img, 3, 7, 21)

# Show
cv2.imshow('Modified Image', mod)
showPlot(img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.destroyAllWindows()
