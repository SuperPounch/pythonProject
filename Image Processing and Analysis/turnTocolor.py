#coding=utf-8

'''
 import cv2
 im_gray = cv2.imread("/Users/lx/Downloads/灰色1.jpeg", cv2.IMREAD_GRAYSCALE)
 im_color = cv2.applyColorMap(im_gray, cv2.COLORMAP_JET)
 cv2.imwrite('/Users/lx/Downloads/灰色1.jpeg', im_color)
'''

"""
import cv2
img = cv2.imread('/Users/lx/Downloads/灰色1.jpg',2)
im_gray = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
im_color = cv2.applyColorMap(im_gray, cv2.COLORMAP_JET)
cv2.imwrite('/Users/lx/Downloads/灰色1_1.jpg',im_color)
"""


'''
import cv2
import os.path
import glob
import numpy as np
from PIL import Image

def convertPNG(pngfile, outdir):
	# 读取灰度图
	im_depth = cv2.imread(pngfile)
	# 转换成伪彩色（之前必须是8位图片）
	# 这里有个alpha值，深度图转换伪彩色图的scale可以通过alpha的数值调整，我设置为1，感觉对比度大一些
	im_color = cv2.applyColorMap(cv2.convertScaleAbs(im_depth, alpha=1), cv2.COLORMAP_JET)
	# 转成png
	im = Image.fromarray(im_color)
	# 保存图片
	im.save(os.path.join(outdir, os.path.basename(pngfile)))

for pngfile in glob.glob("/Users/lx/Downloads/灰色1.jpg"):
	convertPNG(pngfile, "/Users/lx/Downloads/灰色1.jpg")
	'''




'''
__author__ = 'Administrator'
import cv
def Color(image):
    w = image.width
    h = image.height
    size = (w,h)
    iColor = cv.CreateImage(size,8,3)
    for i in range(h):
        for j in range(w):
            r = GetR(image[i,j])
            g = GetG(image[i,j])
            b = GetB(image[i,j])
            iColor[i,j] = (r,g,b)
    return iColor

def GetR(gray):
    if gray < 127:
        return 0
    elif gray > 191:
        return 255
    else:
        return (gray-127)*4-1


def GetG(gray):
    if gray < 64:
        return 4*gray
    elif gray > 191:
        return 256-(gray-191)*4
    else:
        return 255

def GetB(gray):
    if gray < 64:
        return 255
    elif gray > 127:
        return 0
    else:
        return 256-(gray-63)*4

def FColor(image,array):
    w = image.width
    h = image.height
    size = (w,h)
    iColor = cv.CreateImage(size,8,3)
    for i in range(h):
        for j in range(w):
            iColor[i,j] = array[int(image[i,j]/16)]
    return iColor

FCArray = [(0,51,0),(0,51,102),(51,51,102),(51,102,51),\
            (51,51,153),(102,51,102),(153,153,0),(51,102,153),\
            (153,102,51),(153,204,102),(204,153,102),(102,204,102),\
            (153,204,153),(204,204,102),(204,255,204),(255,255,204)]
image = cv.LoadImage('18.jpg',0)
iColor = Color(image)
iFColor = FColor(image,FCArray)
cv.ShowImage('image',image)
cv.ShowImage('iColor',iColor)
cv.ShowImage('iFColor',iFColor)
cv.WaitKey(0)
'''