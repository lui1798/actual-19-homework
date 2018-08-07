#首先用import导入random这个模块，用random.randint（0,100）随机生成一个[0,100]之间的整数
#让用户随便输入一个数字，和随机数作比较，如果大了就提示大了，如果小了就提示小了，如果相等，提示猜对了游戏结束
#游戏只有6次机会，没猜一次，减少一次机会同时做出提醒，如果6次都没猜中，提示失败，游戏结束！
#存在一个小问题，当猜到第六次时会提示还有0次机会才会发结束语。

import random
i = random.randint(0,100)
s = 1
while s <= 6:
    a = 6 - s
    s += 1
    o = int(input("Guess which number I'm thinking about now :"))
    if o < i:
        print('Too small ! You have only {} chances left'.format(a))
    elif o > i:
        print('Too big ! You have only {} chances left'.format(a))
    elif o == i:
        print("Guess right, you're awesome!")
        break
    if a == 0:
        print('All six failed , game over!')
        break
