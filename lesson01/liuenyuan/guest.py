#!/usr/bin/env python3
import  random
realnumber = random.randint(0,100)
time = 0
while time <= 5:
    a = int(input("please input a number: "))
    if realnumber < a :
        print("your number is too bigger:")
    elif realnumber >a:
        print("your number is too smaller: ")
    else:
        print("congratulaations!!!! you are right,the number is {}".format(a))
        break
    time += 1
print("the answer is {},sb !!! are you right????? ".format(a))