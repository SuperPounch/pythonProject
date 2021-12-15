import cv2
import numpy as np


def to_gray(path):
    img = cv2.imread(path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img_gray


'''
输入灰度级        输出彩色
 0～63  1/4         蓝色
 64～127 2/4        紫色
 128～191 3/4       黄色
 192～255  4/4      红色
'''


def show(img):
    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def color(img_gray):
    row, col = img_gray.shape[:]
    print(row, col)
    b = np.zeros((row, col))
    print('b', b, b.shape[:])
    g = np.zeros((row, col))
    r = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            if(img_gray[i, j]<255//4):
                b[i, j] = 255
                g[i, j] = 4 * img_gray[i, j]
                while (g[i, j]>255):
                    g[i, j] -= 255
                r[i, j] = 0
            elif(img_gray[i, j]<255//2):
                b[i, j] = -4 * img_gray[i, j]
                while (b[i, j]<0):
                    b[i, j]+=255
                g[i, j] = 255
                r[i, j] = 0
            elif(img_gray[i, j]<3*255//4):
                b[i, j] = 0
                g[i, j] = 255
                r[i, j] = 4*img_gray[i, j]-255*2
                while (r[i, j]>255):
                    r[i, j]-=255
            else:
                b[i, j] = 0
                g[i, j] = -4*img_gray[i, j]+0*255
                while (g[i, j]<0):
                    g[i, j] += 255
                r[i, j] = 255
    img_color = cv2.merge([b, g, r])
    return img_color


img_gray = to_gray('qq.jpg')
img_color = color(img_gray)
show(img_gray)
show(img_color)