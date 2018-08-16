#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : taurusslq
# @Time    : 2018/8/16 下午9:52
# @File    : lesson-2-maopao.py
# @Software: PyCharm


list1 = [3, 7, 8, 5, 20, 11]

print(list1)
num = len(list1)-1

for j in range(len(list1)):
    for i in range(num):
        if list1[i] > list1[j]:
            list1[i],list1[j] = list1[j],list1[i]
print(list1)
