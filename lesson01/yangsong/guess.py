# -*- coding: utf-8 -*-
import random

n = 1
rightnum = random.randint(1, 100)
while n < 7:
    n += 1
    guessnum = int(input("请输入一个一百以内的整数： "))
    if n == 7:
        print("次数用完了")
        break
    if guessnum == rightnum:
        print("猜对了")
    elif guessnum > rightnum:
        print("大了")
    elif guessnum < rightnum:
        print("小了")
