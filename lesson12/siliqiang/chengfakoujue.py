#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : taurusslq
# @Time    : 2018/11/17 上午12:21
# @File    : chengfakoujue.py
# @Software: PyCharm

n = 1
m = 1
j = 1

while j < 10:
    j += 1
    while n < j:
        print ("{} x {} = {}".format(n,m,m*n),end=" ")
        n += 1
    print()
    m += 1
    n = 1

###########################################################
for m in range(1, 10):
    for n in range(1, m + 1):
        outcome = m * n
        print("{} x {} = {}".format(m, n, outcome), end=' ')
    print()