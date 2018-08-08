#! /usr/bin/python
# -*- coding: utf-8 -*-
# @File  : numbergame.py
# @Author: ZhouGui
# @Date  : 2018/8/6
import random

count = 0
number = random.randint(0, 100)
while count < 6:
    inputNumber = input("Please input your number:")
    if inputNumber.isdigit() == False:
        print("请输入整数!!!")
        continue
    if int(inputNumber) == number:
        print("Congratulations, you guessed it.")
        break
    elif int(inputNumber) > number:
        print("Sorry, you guessed big,你还有{}次机会!!!".format(5 - count))
    else:
        print("Sorry, you guessed small,你还有{}次机会!!!".format(5 - count))
    count += 1
else:
    print("次数用完了哦，正确数字是%s!!!" % number)
