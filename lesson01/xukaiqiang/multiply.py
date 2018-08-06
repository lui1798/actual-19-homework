#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/6 上午10:52
# @Author  : iteemo
# @File    : multiply.py
"""
99乘法表是已知的循环9次
所以使用for 循环已知的就此 
因为print每次都换号所以使用end='' 禁止换行
这时候 所有的输出都是一行所以也不符合规则,
最外层循环完毕正好是1*9因此需要换行
第二个循环使用i+1是不让每个循环都输出9次
"""
for i in range(1,10):
    for x in range(1,i+1):
        print("%s x %s = %s\t"%(i,x,i*x),end='')
    print('\n')
