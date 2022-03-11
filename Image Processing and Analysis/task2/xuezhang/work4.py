import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    for i in range(5):
        img_in = cv2.imread("{}.jpg".format(i), 0)
        f = np.fft.fft2(img_in)
        fshift = np.fft.fftshift(f)
        img_out = np.log(np.abs(fshift))
        plt.imsave("{}_fft.jpg".format(i),img_out)    
        f1shift = np.fft.ifftshift(fshift)
        img_back = np.fft.ifft2(f1shift)
        img_back = np.abs(img_back)
        plt.imsave("{}_fft_back.jpg".format(i),img_back) 