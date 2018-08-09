#! /usr/bin/python
# -*- coding: utf-8 -*-
# @File  : chengfa.py
# @Author: ZhouGui
# @Date  : 2018/8/6
for i in range(1, 10):
    for m in range(1, 10):
        if m <= i:
            print("{}*{}={}".format(i, m, i * m), end=" ")
    print()
