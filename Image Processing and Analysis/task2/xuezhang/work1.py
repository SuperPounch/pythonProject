import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

def pinyu(im):
    f = np.fft.fft2(im)
    fshift = np.fft.fftshift(f)
    return np.log(np.abs(fshift))

if __name__ == "__main__":
    for i in range(5):
        for D0 in [5, 20, 50, 80, 250]:
            img_in = img.imread("{}_D0={}.jpg".format(i, D0))
            b,g,r = cv2.split(img_in)
            b = pinyu(b)
            plt.imshow(b)
            plt.imsave("{}_D0={}_pinyu.jpg".format(i, D0), b)
            
                
