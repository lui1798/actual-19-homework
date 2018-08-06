#coding:gbk
'''
1.猜一个100以内的整数
2.6次机会
3.每次猜时，猜对了，大了，小了
提示：生成随机数的方法
import random
random.randint(0, 100)
'''

import random

n = 1
num = random.randint(1,100)
while n <= 6:
    n += 1
    _input = int(input('pls input your num: '))
    if _input == num:
        print('{} = {} 猜对了'.format(_input,num))
    elif _input >= num:
        print('{} > {} 猜大了'.format(_input,num))
    else:
        print('{} < {} 猜小了'.format(_input,num))