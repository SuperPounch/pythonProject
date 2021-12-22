import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/lx/PycharmProjects/pythonProject/Image Processing and Analysis/photo/灰鹦鹉.png', 0)
plt.subplot(321)
plt.imshow(img, 'gray')
plt.title('origial')
plt.xticks([])
plt.yticks([])
# 高通滤波
rows, cols = img.shape
high = np.ones(img.shape, np.uint8)
high[rows // 2 - 30:rows // 2 + 30, cols // 2 - 30:cols // 2 + 30] = 0
# 低通滤波
low = np.zeros(img.shape, np.uint8)
low[rows // 2 - 40:rows // 2 + 40, cols // 2 - 40:cols // 2 + 40] = 1
# DFT
f1 = np.fft.fft2(img)
f1shift = np.fft.fftshift(f1)
high_shift = f1shift * high
low_shift = f1shift * low
# 显示频域处理
high_f = np.log(np.abs(high_shift))
low_f = np.log(np.abs(low_shift))
high_shift = np.fft.ifftshift(high_shift)  # 对high进行逆变换
img_high = np.fft.ifft2(high_shift)
low_shift = np.fft.ifftshift(low_shift)  # 对low进行逆变换
img_low = np.fft.ifft2(low_shift)
# 出来的是复数，无法显示
img_high = np.abs(img_high)
img_low = np.abs(img_low)
# 调整大小范围便于显示
img_high = (img_high - np.amin(img_high)) / (np.amax(img_high) - np.amin(img_high))
img_low = (img_low - np.amin(img_low)) / (np.amax(img_low) - np.amin(img_low))
plt.subplot(323)
plt.imshow(img_high, 'gray')
plt.title('Highpass')
plt.xticks([])
plt.yticks([])
plt.subplot(324)
plt.imshow(img_low, 'gray')
plt.title('Lowpass')
plt.xticks([])
plt.yticks([])
plt.subplot(325)
plt.imshow(high_f, 'gray')
plt.title('highpass_f')
plt.xticks([])
plt.yticks([])
plt.subplot(326)
plt.imshow(low_f, 'gray')
plt.title('lowpass_f')
plt.xticks([])
plt.yticks([])
plt.show()
