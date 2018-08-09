#!/usr/bin/python
# mail:haodongz@yeah.net
# _*_ coding:utf-8 _*_ 

import random
s = random.randint(0,100)
cont = 0
#print("正确数字",s)
while True:
    num = int(input("输入1-100数字:"))
    cont +=1
    if cont ==6:
        print("is over")
        break
    if  num > s:
        print("数字输入过大")
    elif num < s:
        print("数字输入过小")
    elif num == s:
        print("猜对了")
        break
