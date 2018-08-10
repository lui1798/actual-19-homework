#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/10 上午10:54
# @Author  : LuoFeng
# @Site    : 
# @File    : guess_num.py.py
# @Software: PyCharm

import random

# define variables
count = 6
random_num = 0

while count > 0:
    count-=1
    random_num = random.randint(1,101)
    guess_num = int(input("Please enter a number within 100：").strip())
    if guess_num == random_num:
        print("\033[32m哇，真厉害，数字是{}，猜对了。\033[0m".format(random_num))
        break

    elif guess_num > random_num:
        print("\033[33m不对哟，太大了，数字是{}，还有{}机会，加油。\033[0m".format(random_num,count))

    else:
        print("\033[33m不对哟，太小了，数字是{}，还有{}机会，加油。\033[0m".format(random_num,count))

    if count == 0:
        print("\033[31m太遗憾了，机会已用完，下次再来。\033[0m")
        break
