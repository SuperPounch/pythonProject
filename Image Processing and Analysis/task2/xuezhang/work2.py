import cv2
import numpy as np 
import matplotlib.pyplot as plt

def GaussianFrequencyFilter(src, sigma = 1): 	
	
    imarr = np.array(src) 	
    
    height, width = imarr.shape 	
    fft = np.fft.fft2(imarr)	
    fft = np.fft.fftshift(fft) 	
    for i in range(height):		
        for j in range(height):			
            fft[i, j] *= np.exp(-((i - (height - 1)/2)**2 + (j - (width - 1)/2)**2)/2/sigma**2) 
    fft = np.fft.ifftshift(fft)	
    ifft = np.fft.ifft2(fft) 	
    
    ifft = np.real(ifft)	
    max_1 = np.max(ifft)	
    min_1 = np.min(ifft) 	
    res = np.zeros((height, width), dtype = "uint8") 	
    for i in range(height):		
        for j in range(width):			
            res[i, j] = 255 * (ifft[i, j] - min_1)/(max_1 - min_1) 
    return res
    


if __name__ == "__main__":
    for i in range(5):
        for D0 in [5, 20, 50, 80, 250]:
            img_in = cv2.imread("{}.jpg".format(i))
            b,g,r = cv2.split(img_in)
            res = cv2.merge([GaussianFrequencyFilter(r, D0), GaussianFrequencyFilter(g, D0), GaussianFrequencyFilter(b, D0)])
            plt.imsave("{}_D0={}.jpg".format(i, D0), res)

