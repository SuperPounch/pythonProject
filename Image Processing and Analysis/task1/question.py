import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image
import cv2


ima = image.imread('3.jpg')
plt.figure(figsize=(20,12))

plt.subplot(2,2,1)
plt.imshow(ima)

plt.subplot(2,2,3)
a = -1
kernel = np.array([[0, a, 0], [a, 4, a], [0, a, 0]] , np.float32) #定义一个核
ima_out = cv2.filter2D(ima, -1, kernel=kernel) 
plt.imshow(ima_out)
