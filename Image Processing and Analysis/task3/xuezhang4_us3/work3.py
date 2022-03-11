import cv2
import numpy as np
import matplotlib.pyplot as plt

for i in range(5):
    img = cv2.imread("{}.jpg".format(i), 0)
    text = np.array(img)
    text = text.reshape(-1)
    
    text_RLE = text.copy()
    for j in range(len(text)-10):
        text_RLE[j] = np.mean(text[j+1:j+10])
    text_RLE = np.array(text_RLE)
    print("origin:{}, RLE:{}".format(text.shape, text_RLE.shape))
