import cv2 
import numpy as np
from matplotlib import pyplot as plt


def fft(img, D0):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    rows, cols = img.shape
    crow,ccol = int(rows/2), int(cols/2)
    fshift[crow-D0:crow+D0, ccol-D0:ccol+D0] = 0
    ishift = np.fft.ifftshift(fshift)
    iimg = np.fft.ifft2(ishift)
    iimg = np.abs(iimg)
    return iimg

if __name__ == "__main__":
    for i in range(5):
        img_in = cv2.imread('{}.png'.format(i))
        b, g, r = cv2.split(img_in)
        for D0 in [120]:
            plt.imsave('{}_D0={}.png'.format(i,D0),fft(b, D0))

            
            
            
            
            
            
            