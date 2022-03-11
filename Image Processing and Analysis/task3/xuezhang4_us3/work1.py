import cv2
import numpy as np
import matplotlib.pyplot as plt

for i in range(5):
    img = cv2.imread("{}.jpg".format(i), 0)
    text = np.array(img)
    text = text.reshape(-1)
    
    
    text_RLE = []
    nums = 0
    for j in range(len(text)):
        if j == 0 :
            nums = 1
        elif text[j] == text[j-1]:
            nums += 1
        else :
            text_RLE.append(nums)
            text_RLE.append(text[j-1])
            nums = 1
    text_RLE = np.array(text_RLE)
    
    print("origin:{}, RLE:{}, yasuolv:{}".format(text.shape, text_RLE.shape,text_RLE.shape[0]/text.shape[0]))
