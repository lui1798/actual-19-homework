#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/10 下午1:47
# @Author  : LuoFeng
# @Site    : 
# @File    : multi_table.py.py
# @Software: PyCharm

# 长方形乘法表
for x in range(1,10):
    for y in range(1,10):
        multi_res = x * y
        print("{} x {} = {}".format(x,y,multi_res),end="\t")
    print(" ")

# 左下三角乘法表
for x in range(1,10):
    for y in range(1,x+1):
        multi_res = x * y
        print("{} x {} = {}".format(x,y,multi_res),end=" ")
    print(" ")
