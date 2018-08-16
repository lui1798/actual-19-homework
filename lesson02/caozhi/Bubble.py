#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author emmby,2018-08-15
# 输入n个整数，冒泡法排序
s = []
n = abs(int(input('\033[31minput times: \033[0m')))
for m in range(n):
    k = int(input('\033[33minput a number: \033[0m'))
    s.append(k)
for i in range(len(s) - 1):
    for j in range(len(s) - i - 1):
        if s[j] > s[j+1]:
            s[j], s[j+1] = s[j+1], s[j]
print(s)
