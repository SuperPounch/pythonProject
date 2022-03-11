from PIL import Image
from PIL import ImageEnhance
import cv2

import matplotlib.pylab as plt
import numpy as np

image = Image.open("/Users/lx/PycharmProjects/pythonProject/Image Processing and Analysis/photo/灰花2.jpeg")
enh_con = ImageEnhance.Contrast(image)
contrast = 3
image_contrasted = enh_con.enhance(contrast)
#image_contrasted.show()
image_contrasted.save("image_contrasted2.jpg")

image = cv2.imread("/Users/lx/PycharmProjects/pythonProject/Image Processing and Analysis/photo/灰花2.jpeg", 0)
hist = cv2.calcHist([image], [0], None, [256], [-0.0001, 255.0])
plt.figure(0)
plt.plot(hist)
plt.savefig("hist.jpg")

m, n = image.shape
arr = np.zeros_like(image)
for i in range(m):
    for j in range(n):
        if image[i, j] > 200: #阈值
            arr[i, j] = 255

cv2.imwrite("binary.jpg", arr)





