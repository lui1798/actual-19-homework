#随机数
import random

a = random.randint(0, 100)
n = 0
while n < 6:
    b = eval(input('please input a integer from 1 to 100: '))
    n += 1
    if isinstance(b, int) and b > 0:
        if a < b:
            print('大了')
        elif a > b:
            print('小了')
        else:
            print('猜对了')
    else:
        print('输入错误，请重新输入')
if a != b:
    print('正确的数是%s' % a)

#99乘法
for i in range(1,10):
    for j in range(1,i+1):
        print('%d * %d = %d\t' % (i,j,i*j),end=' ')
    print(' ')
