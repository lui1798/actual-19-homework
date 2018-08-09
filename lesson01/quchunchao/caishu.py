#!/Users/linux/miniconda3/bin/pytho/usr/bin/pythonn

import random

n = random.randint(0, 100)
frequency = 6
while frequency > 0:
    num = int(input("请输入一个数字:"))
    if num > n:
        print(num, "大了，剩余{}次机会".format(frequency-1))
    elif num < n:
        print(num, "小了，剩余{}次机会".format(frequency-1))
    else:
        print(num, "猜对")
        break
    frequency -= 1
