#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time          : 2018/8/5 下午8:39
# Author        : Yuhao.Wang
# FileName      : hmw_random-students.py
# Description   :
#

import random
# 生成一个姓名队列 以 student开头
st_list = ['student' + str(x) for x in range(1, 21)]

# 随机生成 一个 8 人的 学生队列
n = 0
while n < 8:
    luck = random.randint(0, len(st_list) - 1)
    print(st_list[luck])
    st_list.pop(luck)
    n += 1
