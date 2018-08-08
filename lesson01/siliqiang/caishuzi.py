#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
num = random.randint(0, 100)
n = 1
print(num)
yournum = int(input("请输入你猜的数字(你有六次机会): "))
while n < 6:
    if num == yournum:
        print("恭喜你猜对了！")
    elif num > yournum:
        yournum = int(input("你猜小了，请新输入: "))
    else:
        yournum = int(input("你猜大了，请新输入: "))
    n += 1
if num == yournum:
    print("恭喜你猜对了！")
else:
    print("你的机会已用完！")


