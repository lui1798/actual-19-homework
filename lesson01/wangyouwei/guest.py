#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-7 上午9:07
# @Author  : Uwei
# @File    : guest.py
import random

Answer = random.randint(0, 100)
Tries = 6
print('<<<<<<<猜数字游戏开始>>>>>>>>')
while Tries > 0:
    Guest = int(input("请输入一个数字:"))
    if Guest > Answer:
        print(Guest, "猜大了，还剩{}次机会".format(Tries-1))
    elif Guest < Answer:
        print(Guest, "猜小了，还剩{}次机会".format(Tries-1))
    else:
        print(Guest, "猜对了!!!!!!!!!")
        break
    Tries -= 1
print('<<<<<<<猜数字游戏结束>>>>>>>>')
