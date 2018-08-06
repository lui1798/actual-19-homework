#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-6 下午5:09
# @Author  : Uwei
# @File    : chengfa.py
for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}'.format(i,j,i*j),end=' ')
    print()