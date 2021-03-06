from PIL import Image;
import cv2;
import numpy as np;
from itertools import chain

# from compiler.ast import flatten
import sys
import math;
import operator;
from functools import reduce;

# image1 = Image.open('./test/8-10.png');
# image2 = Image.open('./test/test.png');
# histogram1 = image1.histogram()
# histogram2 = image2.histogram()
#
# differ = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, histogram1, histogram2))) / len(histogram1))
#
# print(differ)
import os


def pHash(imgfile):
    """get image pHash value"""
    # 加载并调整图片为32x32灰度图片
    img = cv2.imread(imgfile, 0)
    img = cv2.resize(img, (32, 32), interpolation=cv2.INTER_LANCZOS4  )

    # 创建二维列表
    h, w = img.shape[:2];
    vis0 = np.zeros((h, w), np.float32)
    vis0[:h, :w] = img  # 填充数据

    # 二维Dct变换
    vis1 = cv2.dct(cv2.dct(vis0))
    # cv.SaveImage('a.jpg',cv.fromarray(vis0)) #保存图片
    vis1.resize(32, 32)

    # 把二维list变成一维list
    img_list = np.array(vis1.tolist()).flatten('F');
    # 计算均值
    avg = sum(img_list) * 1. / len(img_list)
    avg_list = ['0' if i < avg else '1' for i in img_list]

    # 得到哈希值
    return ''.join(['%x' % int(''.join(avg_list[x:x + 4]), 2) for x in range(0, 32 * 32, 4)])


def hammingDist(s1, s2):
    assert len(s1) == len(s2)
    return sum([ch1 != ch2 for ch1, ch2 in zip(s1, s2)])


path = "./test/"
files = os.listdir(path);
print(files)
for filename in files:
    HASH1 = pHash(path + '/' + filename)
    HASH2 = pHash('./test.png')
    out_score = 1 - hammingDist(HASH1, HASH2) * 1. / (32 * 32 / 4)
    print(filename, out_score)
