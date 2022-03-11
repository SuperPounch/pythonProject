import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image

def Laplace_suanzi(img):
    r, c = img.shape
    new_image = np.zeros((r, c))
    L_sunnzi = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])      
    # L_sunnzi = np.array([[1,1,1],[1,-8,1],[1,1,1]])       
    for i in range(r-2):
        for j in range(c-2):
            new_image[i+1, j+1] = np.sum(img[i:i+3, j:j+3] * L_sunnzi) + img[i+1, j+1]
            if new_image[i+1, j+1] >255:
                new_image[i+1, j+1] = 255
            elif new_image[i+1, j+1] < 0:
                new_image[i+1, j+1] = 0            
    return np.uint8(new_image)
 
def sobel_suanzi(img):
    r, c = img.shape
    new_image = np.zeros((r, c))
    new_imageX = np.zeros(img.shape)
    new_imageY = np.zeros(img.shape)
    s_suanziX = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])      # X方向
    s_suanziY = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])      
    for i in range(r-2):
        for j in range(c-2):
            new_imageX[i+1, j+1] = abs(np.sum(img[i:i+3, j:j+3] * s_suanziX))
            new_imageY[i+1, j+1] = abs(np.sum(img[i:i+3, j:j+3] * s_suanziY))
            new_image[i+1, j+1] = (new_imageX[i+1, j+1]*new_imageX[i+1,j+1] + new_imageY[i+1, j+1]*new_imageY[i+1,j+1])**0.5
            new_image[i+1, j+1] +=  new_image[i+1, j+1] + img[i+1, j+1]
            if new_image[i+1, j+1] >255:
                new_image[i+1, j+1] = 255
            elif new_image[i+1, j+1] < 0:
                new_image[i+1, j+1] = 0  
    return np.uint8(new_image)  # 无方向算子处理的图像`

def my_suanzi(img):
    r, c = img.shape
    new_image = np.zeros((r, c))
    my_sunnzi = np.array([[-1,0,0],[0,2,0],[0,0,-1]])     
    for i in range(r-2):
        for j in range(c-2):
            new_image[i+1, j+1] = np.sum(img[i:i+3, j:j+3] * my_sunnzi) + img[i+1, j+1]
            if new_image[i+1, j+1] >255:
                new_image[i+1, j+1] = 255
            elif new_image[i+1, j+1] < 0:
                new_image[i+1, j+1] = 0       
    return np.uint8(new_image)    

def main():
    for i in range(1):
        ima = image.imread('{}.jpg'.format(i))
        ima_out = ima.copy()
        ima_out[:,:, 0] = Laplace_suanzi(ima_out[:,:, 0] )
        ima_out[:,:, 1] = ima_out[:,:, 0] 
        ima_out[:,:, 2] = ima_out[:,:, 0] 
        plt.imshow(ima_out)








