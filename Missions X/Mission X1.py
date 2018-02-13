import cv2
import numpy as np
from matplotlib import pyplot as plt


def showPlot(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show()


img = cv2.imread('img/Dark Side of the Moon.png', 0)

# Fourier
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
ms = 20 * np.log(np.abs(fshift))

# Fourier Inverse
ishift = np.fft.ifftshift(fshift)
ifour = np.abs(np.fft.ifft2(ishift))

# Plots
plt.subplot(131)
plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(132)
plt.imshow(ms, cmap='gray')
plt.title('Spectrum'), plt.xticks([]), plt.yticks([])

plt.subplot(133)
plt.imshow(ifour, cmap='gray')
plt.title('Inverse'), plt.xticks([]), plt.yticks([])

plt.show()
