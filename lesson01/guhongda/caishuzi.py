#encoding:utf-8
#  猜数游戏
# 随机生成一个0到100的数字，提示用户在控制台上输入一个数字
# 当用户输入数字小于生成的随机数，则打印猜小了
# 当用户输入数字大于生成的随机数，则打印猜大了
# 当用户输入数字等于生成的随机数，则打印猜对了，结束程序
# 用户最可猜测5次，如果5次都错误，则打印“太笨了，下次再来”，并结束程序

import random

random_num = random.randint(0,3)
count = 1
while count < 6:
    name = int(input('请随机输入一个数字：'))
    if name > random_num:
        print('猜大了')
    elif name < random_num:
        print('猜小了')
    else:
        print('猜对了')
        break
    count += 1
if count >= 6:
    print('太笨了，下次再来')
