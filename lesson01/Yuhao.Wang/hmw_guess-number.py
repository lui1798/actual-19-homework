#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time          : 2018/8/5 下午8:34
# Author        : Yuhao.Wang
# FileName      : hmw_guess-number.py
# Description   :
#
import random

true_number = random.randint(1, 101)
n = 6
while True:
    guess = int(input('猜猜是多少?(还有 %d 次机会哟): ' % n))
    use_times = 6 - n + 1
    if guess > true_number:
        print('猜大了!!')
    elif guess < true_number:
        print('猜小了!!')
    else:
        if use_times == 1:
            print('Bingo!! 牛逼了兄弟,今日万事大吉!!')
        elif use_times <= 3:
            print('可以的兄弟! %d 次就猜出来了!' % use_times)
        else:
            print('好险啊 = =,差点没猜出!')
        break
    if n > 1:
        n -= 1
    else:
        print('哈哈,真正的数字是 %d,下次再来!' % true_number)
        break
