# -*- coding: utf-8 -*-

"""
Author  : htfeng
Date    : 20180626
Content : 画出台站统计结果
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *


# 为柱状图添加数字
def autoLabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.-0.2, 1.02*height, '%s' % int(height))


# 查看文件夹是否存在，不存在则创建
def mkdir(img):
    if not os.path.exists(img):
        os.mkdir(img)


# 按年份IVS和CVN观测统计图
def plot_1(data):
    IVS = []
    CVN = []
    year = []
    for i in range(len(data)):
        IVS.append(data.iloc[i, 1:].sum())  # 对某一行进行求和
        CVN.append(data.iloc[i, 1:].sum())  # 对某一行进行求和
        year.append(data.year[i])

    total_width, n = 0.8, 2
    width = total_width / n

    plt.figure(figsize = [15.0, 8.0], dpi = 100)
    a = plt.bar(year, IVS, width= width, label = 'IVS', fc = 'b')
    autoLabel(a)
    for i in range(len(year)):
        year[i] = year[i] + width
    b = plt.bar(year, CVN, width= width, label = 'CVN', tick_label = year, fc = 'r')
    autoLabel(b)
    plt.title(station)
    plt.legend()   # 显示标签
    startYear = data.ix[0].year
    endYear = data.ix[n - 1].year
    plt.xlabel(u"{0}站{1}-{2}年观测统计(按观测类型)".format(station, startYear, endYear))
    plt.savefig(img_station + station + '.png', dpi = 200)
    plt.show()


# 按观测类型
def dropCol(data):
    countType = {}  # 存放台站参与观测的类型
    dropCol = []  # 全部为零的列的索引
    for i in range(len(data.apply(sum))):
        key = data.apply(sum).keys()[i]
        value = data.apply(sum).values[i]  # apply函数获取每列数据的和
        if (i > 0 and value == 0) or key == 'year':
            dropCol.append(key)    # 保存全部为零的列的索引
        if i > 0 and value > 0:
            countType[key] = value
    df = data.drop(dropCol, axis = 1)  # 删除全部为零的列

    return df


def plot_2(data):
    df = dropCol(data)
    total_width, n = 1, len(df)
    width = total_width / n
    center = int(n/2)         # 在中间设置横坐标
    x = []
    for i in range(len(df.ix[0])):
        x.append(i*1.5)
    plt.figure(figsize = [15.0, 8.0], dpi = 100)
    for j in range(n):
        for i in range(len(x)):
            x[i] = x[i] + width
        if j != center:
            plt.bar(x, height = df.ix[j], width = width, align='center', label = data.ix[j].year)
        if j == center:
            plt.bar(x, height = df.ix[j], width = width, align = 'center', label = data.ix[j].year, tick_label = df.keys())
    plt.legend()
    plt.grid()
    plt.title(station)
    startYear = data.ix[0].year
    endYear = data.ix[n-1].year
    plt.xlabel(u"{0}站{1}-{2}年观测统计(按观测类型)".format(station, startYear, endYear))
    plt.savefig(img_station + '{}-{}.png'.format(startYear, endYear))
    plt.show()


# 每一年每种观测类型
def plot_3(data):
    df = dropCol(data)
    for i in range(len(df)):
        plt.figure(figsize = [15.0, 8.0], dpi = 100)
        title = data.ix[i].year
        a = plt.bar(df.keys(), df.ix[i])
        plt.title('{0}({1})'.format(station, title))
        autoLabel(a)
        plt.xlabel(u"{0}站{1}年观测统计".format(station, title))
        plt.savefig(img_station + '{0}.png'.format(title))
        plt.clf()
        plt.close()


if '__main__' == __name__:
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文

    img = os.getcwd() + "\\img\\"
    mkdir(img)
    stations = ['Sh', 'Km', 'Ur']

    for station in stations:
        img_station = os.getcwd() + "\\img\\" + station + "\\"
        data = pd.read_table('result/' + station + '.txt', delim_whitespace = True)
        data.set_index('year')

        mkdir(img_station)

        plot_1(data)
        plot_2(data)
        plot_3(data)

"""
# 折线图
plt.plot(data.year, data.R1,  marker="*", linewidth=3, linestyle="--", color="orange")
plt.plot(data.year, data.R4)
plt.title("Sh stations")
plt.ylabel("Nums")
plt.xlabel("year")

plt.legend(['R1', 'R4'], loc = "upper right")
plt.grid(True)
plt.show()

# 散点图
plt.scatter(data.year, data.R1)
plt.scatter(data.year, data.R4)
plt.show()

# 柱状图
plt.bar(data.year, data.R1)
plt.bar(data.year, data.R4)
plt.show()
"""
# 饼图
"""
plt.pie(data.year, data.R1)
plt.pie(data.year, data.R4)
plt.show()
"""

# 直方图
"""
plt.hist(data.year, data.R1)
plt.hist(data.year, data.R4)
plt.show()
"""
"""
# 子图
# figsize绘图对象的宽度和高度，单位为英寸，dpi绘图对象的分辨率，即每英寸多少个像素，缺省值为80
plt.figure(figsize=(8, 6), dpi=100)

# subplot(numRows, numCols, plotNum)
# 一个Figure对象可以包含多个子图Axes，subplot将整个绘图区域等分为numRows行*numCols列个子区域，按照从左到右，从上到下的顺序对每个子区域进行编号
# subplot在plotNum指定的区域中创建一个子图Axes
A = plt.subplot(2, 2, 1)
plt.bar(data.year, data.R1, color="red")

plt.subplot(2, 2, 2)
plt.title("B")
plt.bar(data.year, data.R4, color="green")

plt.subplot(2, 1, 2)
plt.title("C")
plt.bar(data.year, data.T2, color="orange")

# 选择子图A
plt.sca(A)
plt.title("A")

plt.show()
"""