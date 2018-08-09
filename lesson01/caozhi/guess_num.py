#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author emmby,2018-08-06
import random
num = random.randint(0,100)
i = 1
while i < 7:
    mynum = int(input("input a number: "))
    if mynum == num:
        print("good!num is %d" % (num))
        break
    elif mynum > num:
        print("大了，try again,the no.%d times loss" % (i))
    else:
        print("小了，try again,the no.%d times loss" % (i))
    i += 1
if i == 7:
    print("\033[31m you have no chance! \033[0m")
