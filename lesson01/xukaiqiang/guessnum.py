#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/6 上午10:49
# @Author  : iteemo
# @File    : guessnum.py
import random
x = random.randint(0,100)
for i in range(1,7):
    m = int(input("please input random number 0-100:"))
    if x == m:
        print("猜对了")
    elif x > m:
        print("猜小了")
    else:
        print("猜大了")
else:
    print("机会使用完毕")
    print("随机数是:%s"%(x))
