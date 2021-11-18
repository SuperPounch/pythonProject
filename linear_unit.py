#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import print_function

import matplotlib.pyplot

from Perceptron import Perceptron

# 定义激活函数f
f = lambda x: x


class LinearUnit(Perceptron):
    def __init__(self, input_num):
        '''初始化线性单元，设置输入参数的个数'''
        Perceptron.__init__(self, input_num, f)


def get_training_dataset():
    '''
    捏造5个人的收入数据
    '''
    # 构建训练数据
    # 输入向量列表，每一项是工作年限
    input_vecs = [[5], [3], [8], [1.4], [10.1]]
    # 期望的输出列表，月薪，注意要与输入一一对应
    labels = [5500, 2300, 7600, 1800, 11400]
    return input_vecs, labels


def train_linear_unit():
    '''
    使用数据训练线性单元
    '''
    # 创建感知器，输入参数的特征数为1（工作年限）
    lu = LinearUnit(1)
    # 训练，迭代10轮, 学习速率为0.01
    input_vecs, labels = get_training_dataset()
    lu.train(input_vecs, labels, 10, 0.01)
    # 返回训练好的线性单元
    return lu


def plot(linear_unit):
    import matplotlib.pyplot as plt
    input_vecs, labels = get_training_dataset()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(map(lambda x: x[0], input_vecs), labels)
    weights = linear_unit.weights
    bias = linear_unit.bias
    x = range(0, 12, 1)
    y = map(lambda x: weights[0] * x + bias, x)
    ax.plot(x, y)
    plt.show()


if __name__ == '__main__':
    '''训练线性单元'''
    linear_unit = train_linear_unit()
    # 打印训练获得的权重
    print(linear_unit)
    # 测试
    print('Work 3.4 years, monthly salary = %.2f' % linear_unit.predict([3.4]))
    print('Work 15 years, monthly salary = %.2f' % linear_unit.predict([15]))
    print('Work 1.5 years, monthly salary = %.2f' % linear_unit.predict([1.5]))
    print('Work 6.3 years, monthly salary = %.2f' % linear_unit.predict([6.3]))
# 报错1：
# RuntimeError: matplotlib does not support generators as input
# 翻译：RuntimeError：matplotlib不支持将生成器作为输入
# 原因：map() 会根据提供的函数对指定序列做映射

#报错2：
# in <module> class LinearUnit(Perceptron): TypeError: module() takes at most 2 arguments (3 given)
# python3在使用类继承时，遇到错误TypeError: module.init() takes at most 2 arguments (3 given)
# https://blog.csdn.net/qq_41538097/article/details/108802048
# 错误原因：此处想要导入类，如上代码所示只是导入了模块，Python的模块名与类名是在两个不同的名字空间中，初学者很容易将其弄混淆。
    # python 类：用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例
    # python 模块：模块，在Python可理解为对应于一个文件。
    # 根据上面代码"import Parent"，你想使用 import Parent 导入Parent 类，但 import Parent 只能导入模块，所以错误
# 方法一
# 使用正确方式导入类， import Parent from Parent (此操作就是导入Parent 模块中的 Parent 类)
# 方法二
# 修改 class Child(Parent): 代码为 class Child(Parent.Parent):，目的也是选中模块中的类
