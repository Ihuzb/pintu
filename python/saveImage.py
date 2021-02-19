# -*- coding: utf-8 -*-
from PIL import Image;
import sys, time;

# 读取文件，获取文件信息
img = Image.open('./pintu.png');
# 获取文件长和宽
width, height = img.size;
# 列数，行数
row_num = 40;
col_num = 25;
# 每一个的长和宽
width_item = width / row_num;
height_item = height / col_num;
total = 0;
for col in range(0, col_num):
    for row in range(0, row_num):
        box = img.crop((row * width_item, col * height_item, (row + 1) * width_item, (col + 1) * height_item));
        box.save('./image/' + str(col) + '-' + str(row) + '.png', 'PNG');
        total = round(total + (100 / (row_num * col_num)), 2)
        sys.stdout.write('\r%s%%' % (total))
        sys.stdout.flush()
print(' ok');
