#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time          : 2018/8/5 下午7:53
# Author        : Yuhao.Wang
# FileName      : hmw_multi-table.py
# Description   :
#

# 长方形
for i in range(1, 10):
    for j in range(1, 10):
        print('%dx%d=%d' % (i, j, i * j), end=' ')
    print('\n')

# 左三角
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%dx%d=%2d' % (i, j, i * j), end=' ')
    print('\n')

# 右三角
for i in range(1, 10):
    counter = '       '
    print(counter * (10 - i), end='')
    for j in range(1, i + 1):
        print('%dx%d=%2d ' % (i, j, i * j), end='')
    print('')
