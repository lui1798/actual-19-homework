#九九乘法表
m=1
while m < 10:
    for n in range(1,m+1):
        if n == m :
            end = '\n'
        else:
            end = '|'

        print("{}x{}={}".format(n,m,m*n),end='{}'.format(end))
    m += 1


#猜数游戏
import random
r = random.randint(0,100)
chance = 6

while chance > 0 :
    num = int(input("You have {} chances.Please enter your guess number : ".format(chance)))
    chance -= 1
    if num == r:
        print("\033[32mCongratulations, guessed it!!\033[0m")
        break
    elif num > r:
        result = 'bigger'
    else:
        result = 'smaller'
    print("your number is %s"%result)