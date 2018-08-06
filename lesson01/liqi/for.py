#!/usr/bin/env python
import random

for x in range(0,6):
    put = int(input('please:'))
    shu = random.randint(0,100)
    if put == shu:
        print('猜对了')
        print(shu)
        break
    elif put > shu:
        print('大了')
    else:
        print('小了')
    if x == 5:
        print('猜题结束')