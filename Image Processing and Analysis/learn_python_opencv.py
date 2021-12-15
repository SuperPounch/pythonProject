#coding=utf-8
# -*- coding:utf-8 -*-
import cv2

'''
1、opencv 读图像主要调用函数如下：
img = cv2.imread(文件名,[,参数])
参数(1) cv2.IMREAD_UNCHANGED (图像不可变)
参数(2) cv2.IMREAD_GRAYSCALE (灰度图像)
参数(3) cv2.IMREAD_COLOR (读入彩色图像)
参数(4) cv2.COLOR_BGR2RGB (图像通道BGR转成RGB)
————————————————————————
2、显示图像
cv2.imshow(窗口名, 图像名)
————————————————————————
3、窗口等待
cv2.waitKey(delay)
键盘绑定函数，共一个参数，表示等待毫秒数，将等待特定的几毫秒，看键盘是否有输入，返回值为ASCII值。如果其参数为0，则表示无限期的等待键盘输入；参数>0表示等待delay毫秒；参数<0表示等待键盘单击。
——————————————————————————
4、删除所有窗口
cv2.destroyAllWindows() 删除所有窗口
cv2.destroyWindows() 删除指定的窗口
————————————————————————————
5、写入图片
retval = cv2.imwrite(文件地址, 文件名)
————————————————————————————

版权声明：本文为CSDN博主「Eastmount」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Eastmount/article/details/81748802
'''

# Opencv像素处理
# 1、读取像素

img=cv2.imread('/Users/lx/Downloads/灰色1.jpeg',cv2.IMREAD_GRAYSCALE)

'''
cv2.imshow("gray",img)
#无限期等待输入
k=cv2.waitKey(0)
#如果输入ESC退出
if k==27:
    cv2.destroyAllWindows()
#在窗口界面，点击esc即为k=27请求退出，再去Python Console
'''
cv2.imwrite("/Users/lx/Downloads/gray2_2.jpeg",img)
