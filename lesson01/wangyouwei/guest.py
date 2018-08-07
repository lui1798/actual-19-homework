#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-7 上午9:07
# @Author  : Uwei
# @File    : guest.py
import random

Answer=27
Tries=6
print('<<<<<<<游戏开始>>>>>>>>')
while Tries > 0:
    Guest=random.randint(0,100)
    if Guest > Answer:
        print(Guest,"猜大了")
    if Guest < Answer:
        print(Guest,"猜小了")
    if Guest == Answer:
        print(Guest,"猜对了!!!!!!!!!")
        break
    Tries = Tries - 1
print('<<<<<<<游戏结束>>>>>>>>')