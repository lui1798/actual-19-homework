#!/usr/bin/env python
import random

n = 0
while n < 6:
    sun = int(input('please:'))
    shu = random.randint(0,100)
    n += 1
    print(shu)
    if sun == shu:
        print('猜对了')
        print(shu)
        break
    elif sun > shu:
        print('大了')
    else:
        print('小了')
    if n == 6:
        print('猜题结束')