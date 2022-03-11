import cv2
import numpy as np
import matplotlib.pyplot as plt


# 整张图 DCT 变换
def whole_img_dct(img_f32):
    img_dct = cv2.dct(img_f32)            # 进行离散余弦变换
    img_dct_log = np.log(abs(img_dct))    # 进行log处理
    img_idct = cv2.idct(img_dct)          # 进行离散余弦反变换
    return img_dct_log, img_idct

# 分块图 DCT 变换
def block_img_dct(img_f32):
    height,width = img_f32.shape[:2]
    block_y = height // 8
    block_x = width // 8
    height_ = block_y * 8
    width_ = block_x * 8
    img_f32_cut = img_f32[:height_, :width_]
    img_dct = np.zeros((height_, width_), dtype=np.float32)
    new_img = img_dct.copy()
    for h in range(block_y):
        for w in range(block_x):
            # 对图像块进行dct变换
            img_block = img_f32_cut[8*h: 8*(h+1), 8*w: 8*(w+1)]
            img_dct[8*h: 8*(h+1), 8*w: 8*(w+1)] = cv2.dct(img_block)

            # 进行 idct 反变换
            dct_block = img_dct[8*h: 8*(h+1), 8*w: 8*(w+1)]
            img_block = cv2.idct(dct_block)
            new_img[8*h: 8*(h+1), 8*w: 8*(w+1)] = img_block
    img_dct_log2 = np.log(abs(img_dct))
    return img_dct_log2, new_img
#更改dct系数
def block_img_dct2(img_f32):
    height,width = img_f32.shape[:2]
    block_y = height // 8
    block_x = width // 8
    height_ = block_y * 8
    width_ = block_x * 8
    img_f32_cut = img_f32[:height_, :width_]
    img_dct = np.zeros((height_, width_), dtype=np.float32)
    new_img = img_dct.copy()
    for h in range(block_y):
        for w in range(block_x):
            # 对图像块进行dct变换
            img_block = img_f32_cut[8*h: 8*(h+1), 8*w: 8*(w+1)]
            img_dct[8*h: 8*(h+1), 8*w: 8*(w+1)] = cv2.dct(img_block)
            img_dct[8*h, 8*w] = np.float32(100) * h
            #img_dct[8 * h+4: 8 * (h + 1), 8 * w+4: 8 * (w + 1)] = np.zeros((4, 4), dtype=np.float32)
            #img_dct[8 * h + 4: 8 * (h + 1), 8 * w + 4: 8 * (w + 1)] = 20 * np.ones((4, 4), dtype=np.float32)
            # 进行 idct 反变换
            dct_block = img_dct[8*h: 8*(h+1), 8*w: 8*(w+1)]
            img_block = cv2.idct(dct_block)
            new_img[8*h: 8*(h+1), 8*w: 8*(w+1)] = img_block
    img_dct_log2 = np.log(abs(img_dct))
    return img_dct_log2, new_img

if __name__ == '__main__':
    img_u8 = cv2.imread("/Users/lx/PycharmProjects/pythonProject/Image Processing and Analysis/photo/灰鹦鹉.png", 0)
    img_f32 = img_u8.astype(np.float)  # 数据类型转换 转换为浮点型
    img_dct_log, img_idct = whole_img_dct(img_f32)
    img_dct_log2, new_img = block_img_dct(img_f32.copy())
    img_dct_log3, img3 = block_img_dct2(img_f32.copy())
    plt.figure(6, figsize=(12, 8))
    plt.subplot(241)
    plt.imshow(img_u8, 'gray')
    plt.title('original image'), plt.xticks([]), plt.yticks([])
    plt.subplot(242)
    plt.imshow(img_dct_log, 'gray')
    plt.title('DCT'), plt.xticks([]), plt.yticks([])
    plt.subplot(243)
    plt.imshow(img_idct, 'gray')
    plt.title('IDCT'), plt.xticks([]), plt.yticks([])
    plt.subplot(244)
    plt.imshow(img_dct_log2, 'gray')
    plt.title('block_DCT'), plt.xticks([]), plt.yticks([])
    plt.subplot(245)
    plt.imshow(new_img, 'gray')
    plt.title('block_IDCT'), plt.xticks([]), plt.yticks([])

    plt.subplot(246)
    plt.imshow(img_dct_log3, 'gray')
    plt.title('block_DCT2'), plt.xticks([]), plt.yticks([])
    plt.subplot(247)
    plt.imshow(img3, 'gray')
    plt.title('block_IDCT2'), plt.xticks([]), plt.yticks([])

    plt.show()
