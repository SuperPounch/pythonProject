import cv2
import numpy as np
import matplotlib.pyplot as plt


def DCT(img):
    c, v = img.shape
    img_out = img.copy()
    for i in range(c//8):
        for j in range(v//8):
            img_out[i*8:i*8+8, j*8:j*8+8] = cv2.dct(img_out[i*8:i*8+8, j*8:j*8+8].astype(np.float32))
    return img_out

def IDCT(img):
    c, v = img.shape
    img_out = img.copy()
    for i in range(c//64):
        img_out[i*8+7,:] = 0
    for i in range(c//8):
        for j in range(v//8):
            img_out[i*8:i*8+8, j*8:j*8+8] = cv2.idct(img_out[i*8:i*8+8, j*8:j*8+8].astype(np.float32))
    return img_out
    
def GetImg(i):
    img = cv2.imread("{}.jpg".format(i), 0)
    c, v = img.shape
    c = c // 8 * 8
    v = v  // 8 * 8
    return img[:c, :v]
    
if __name__ == "__main__":
    for i in range(5):
        img_in = GetImg(i)
        img_in1 = img_in.copy()
        img_dct = DCT(img_in1)
        plt.imsave("{}_DCT.jpg".format(i),img_dct)
        
        img_idct = IDCT(img_dct)
        plt.imsave("{}_IDCT.jpg".format(i),img_idct)
        
        


