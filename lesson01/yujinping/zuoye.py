# encoding = utf-8
import random


'''打印乘法口诀'''
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}".format(i,j,i*j),end=" ")
    print(" ")



'''猜数游戏：猜一个100以内的整数；6次机会；每次猜时，猜对了，大了，小了'''

num = 1
figure = random.randint(1,100)
print("Please guess the number(number<100), you only get six chances")
# print(figure)
while num <= 6:
    number = int(input("Please input the number:"))

    if number == figure:
        print("猜对了")
        break
    elif number < figure:
        print("小了")
    else:
        print("大了")

    num += 1

