###猜数字
import random as r
num=r.randint(1,100)
print(num)  #测试用
n=1
while n<=6:
    guess_num=int(input("Please input your answer(6 times):"))
    if guess_num==num:
        print("Congratulations!")
        break
    elif guess_num>num:
        print("猜大了！！再来")
    else:
        print("猜小了！！再来")
    n=n+1
