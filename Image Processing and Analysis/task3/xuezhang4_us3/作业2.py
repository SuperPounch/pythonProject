
import matplotlib.pyplot as plt
import tensorflow as tf
import os
import numpy as np
import io

Q = 80


def getbytes(path: np.ndarray):
    return os.path.getsize(path)


def rmse(predictions: np.ndarray, targets: np.ndarray):
    return np.sqrt(((predictions - targets) ** 2).mean())


with tf.Session() as sess:
    for i, img in enumerate(os.listdir('C:\Users\90372\Desktop\homework\digtit\4\'), 0):
        image_raw_data = tf.gfile.FastGFile('C:\Users\90372\Desktop\homework\digtit\4\' + img, 'rb').read()
        # 将图像使用JPEG的格式解码从而得到图像对应的三维矩阵。Tensorflow还提供了 tf.image.decode_png函数对png格式的图像进行编码。
        # 解码之后的结果为一个张量， 在使用他的取值之前需要明确调用运行的过程。
        image_data = tf.image.decode_jpeg(image_raw_data)
        # Decode a JPEG-encoded image to a uint8 tensor 所以这里的 image_data 已经是一个tensor

        """ 解码后为三维矩阵
        print(image_data.eval())
        [[[229 248 246]
          [235 245 246]
          [241 242 247]
          ...
          [238 242 251]
          [238 242 251]
          [238 242 251]]]
        """
        # 使用pyplot工具可视化得到的图像
        # plt.imshow(image_data.eval())
        # plt.show()

        # 将数据的类型转化为实数方便下面的样例程序对图像进行处理
        img_data = tf.image.convert_image_dtype(image_data, dtype=tf.float32)
        ima_data_np = image_data.eval()
        # 将表示一张图像的三维矩阵重新按照jpeg格式编码并存入文件中。打开这张图像就可以得到和原始图像一样的图像
        encoded_image = tf.image.encode_jpeg(image_data, quality=Q)
        encoded_image_np = encoded_image.eval()
        decoded_image = tf.image.decode_jpeg(encoded_image)
        decoded_image_np = decoded_image.eval()
        plt.subplot(2, 5, i)
        plt.axis('off')
        plt.title(f'{img.split(".")[0]}')
        plt.imshow(ima_data_np.astype(np.uint8))

        plt.subplot(2, 5, 5 + i)
        plt.axis('off')

        plt.imshow(decoded_image_np)
        with tf.gfile.GFile(f'./{img.split(".")[0]}.jpg', 'wb') as f:
            f.write(encoded_image_np)
        ratio = getbytes(f'./{img.split(".")[0]}.jpg') / getbytes(f'C:/Users/hasee/Desktop/shuzituxiang/experiment1/111/shiyansi/zuoye2/imgs/{img.split(".")[0]}.jpg')
        plt.title('{} q={} r={:.2f} rmse={:.2f}'.format(img.split(".")[0], Q, ratio, rmse(ima_data_np.astype(np.uint8), decoded_image_np)))
plt.show()
