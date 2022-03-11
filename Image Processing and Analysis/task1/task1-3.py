import numpy as np
import matplotlib.pyplot as plt

def sobel_filter(image):
    h = image.shape[0]
    w = image.shape[1]
    image_new = np.zeros(image.shape, np.uint8)

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            sx = (image[i + 1][j - 1] + 2 * image[i + 1][j] + image[i + 1][j + 1]) - \
                 (image[i - 1][j - 1] + 2 * image[i - 1][j] + image[i - 1][j + 1])
            sy = (image[i - 1][j + 1] + 2 * image[i][j + 1] + image[i + 1][j + 1]) - \
                 (image[i - 1][j - 1] + 2 * image[i][j - 1] + image[i + 1][j - 1])
            image_new[i][j] = np.sqrt(np.square(sx) + np.square(sy))
    return image_new

if __name__ == "__main__":
    img = plt.imread("/Users/lx/PycharmProjects/pythonProject/Image Processing and Analysis/photo/灰色2.jpeg")

    rgb_weight = [0.299, 0.587, 0.114]
    img_gray = np.dot(img, rgb_weight)
    #原图
    plt.subplot(221)
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.title("Original")
    #灰度图
    plt.subplot(222)
    plt.imshow(img_gray, cmap=plt.cm.gray)
    plt.xticks([])
    plt.yticks([])
    plt.title("Gray")
    #Sobel算子
    img_Sobel = sobel_filter(img_gray)
    img_Sobel = img_Sobel.astype(np.float64)
    plt.subplot(223)
    plt.imshow(img_Sobel, cmap=plt.cm.gray)
    plt.xticks([])
    plt.yticks([])
    plt.title("sobel")
    #原图加Sobel算子
    img_final = img_Sobel + img_gray
    plt.subplot(224)
    plt.imshow(img_final, cmap=plt.cm.gray)
    plt.xticks([])
    plt.yticks([])
    plt.title("final")
    plt.show()