import random
n = 1
num1 = random.randint(1, 100)
while True:
    num2 = int(input('Please guess a num: '))
    if num2 == num1:
        print('第{}次猜是very good ,guess right num!'.format(n))
        print('随机数是{}'.format(num1))
        break
    elif num2 > num1:
        print('第{}次猜是太大 了,guess again!'.format(n))
    else:
        print('第{}次猜是太小了 ,guess again'.format(n))
    if n > 5:
        print('第{}次猜了，猜的次数太多了,over!'.format(n))
        print('随机数是{}'.format(num1))
        break
    n += 1

