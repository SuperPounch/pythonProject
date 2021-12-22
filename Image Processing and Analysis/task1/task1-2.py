# 图像去噪平滑滤波
# 使用opencv的自带函数实现，与自编写作比较
# 产生椒盐噪声，高斯噪声等
# 使用中值滤波，平均滤波，高斯滤波，方框滤波

import numpy as np
import cv2
import matplotlib.pyplot as plt
import random

# 向图片中添加椒盐噪声
def salt_pepper_noise(image, prob):  # prob:椒盐噪声阈值，由用户自己决定
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob  # 椒盐噪声阈值
    for i in range(image.shape[0]):  # 遍历整个图片的灰度级
        for j in range(image.shape[1]):
            randomnum = random.random()  # 生成一个随机0-1之间的随机数
            if randomnum < prob:  # 如果随机数大于盐噪声阈值0.1，则将此位置灰度级的值设为0，即添加盐噪声
                output[i][j] = 0
            elif randomnum > thres:  # 如果随机数大于胡椒噪声阈值1-0.1，则将此位置灰度级的输出设为255，即添加胡椒噪声
                output[i][j] = 255
            else:  # 如果随机数处于两者之间，则此位置的灰度级的值等于原图的灰度级值
                output[i][j] = image[i][j]
    return output
# 向图片中添加高斯噪声
def gasuss_noise(image, mean=0, var=0.001):         # mean : 均值，var : 方差
    image = np.array(image/255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)  # 使用numpy库中的函数生成正态分布矩阵，对应数据分别为概率均值，概率标准差，图像的大小
    output = image + noise  # 输出结果为原图灰度级概率与噪声概率相加
    output_handle = np.array([[[0]*3 for i in range(output.shape[1])] for i in range(output.shape[0])], dtype=float)
    # 处理后最终输出矩阵将齐大小设置为与原图一样
    if output.min() < 0:  # 确定一个比较中间值
        low_clip = -1.
    else:
        low_clip = 0.
    for i in range (output.shape[0]):  # 遍历整个三位矩阵
        for j in range (output.shape[1]):
            for k in range (output.shape[2]):
                if output[i][j][k] < low_clip:  # 将输出的概率矩阵内的值限定在(-1,1)范围内
                    output_handle[i][j][k] = low_clip   # 使其之后*255变为灰度级时不会超出[0-255]的范围
                elif output[i][j][k] > 1.0:
                    output_handle[i][j][k] = 1.0
                else:
                    output_handle[i][j][k] = output[i][j][k]    # 在最大值和最小值之间的不变
    output = np.uint8(output_handle*255)   # 将处理后的灰度级转化为[0-255]的整数级
    return output


if __name__ == "__main__":
    image = cv2.imread('/Users/lx/PycharmProjects/pythonProject/Image Processing and Analysis/photo/灰色1.jpeg')

    plt.subplot(3, 3, 1)
    plt.imshow(image)
    plt.axis('off')
    plt.title('Original')

    gauss_img = gasuss_noise(image)
    salt_img = salt_pepper_noise(image, 0.05)

    #高斯噪声
    plt.subplot(3, 3, 2)
    plt.imshow(gauss_img)
    plt.axis('off')
    plt.title('gauss noise')
    #椒盐噪声
    plt.subplot(3, 3, 3)
    plt.imshow(salt_img)
    plt.axis('off')
    plt.title('salt pepper noise')
    # 高斯噪声
    # 高斯滤波 3*3
    result1 = cv2.GaussianBlur(gauss_img, (3, 3), 0)

    plt.subplot(3, 3, 4)
    plt.imshow(result1)
    plt.axis('off')
    plt.title('gaussian 3*3')
    # 高斯滤波 5*5
    result2 = cv2.GaussianBlur(gauss_img, (5, 5), 0)

    plt.subplot(3, 3, 5)
    plt.imshow(result2)
    plt.axis('off')
    plt.title('gaussian 5*5')
    # 高斯滤波 7*7
    result3 = cv2.GaussianBlur(gauss_img, (7, 7), 0)

    plt.subplot(3, 3, 6)
    plt.imshow(result3)
    plt.axis('off')
    plt.title('gaussian 7*7')
    #椒盐噪声
    # 高斯滤波 3*3
    result4 = cv2.GaussianBlur(salt_img, (3, 3), 0)

    plt.subplot(3, 3, 7)
    plt.imshow(result4)
    plt.axis('off')
    plt.title('gaussian 3*3')
    # 高斯滤波 5*5
    result5 = cv2.GaussianBlur(salt_img, (5, 5), 0)

    plt.subplot(3, 3, 8)
    plt.imshow(result5)
    plt.axis('off')
    plt.title('gaussian 5*5')
    # 高斯滤波 7*7
    result6 = cv2.GaussianBlur(salt_img, (7, 7), 0)

    plt.subplot(3, 3, 9)
    plt.imshow(result6)
    plt.axis('off')
    plt.title('gaussian 7*7')

    plt.show()

