#!/bin/python
import random
num = random.randint(1,100)
#print (num)
count = 0
while True:
  count += 1
  if count <=6:
    guessNum = int(input("Enter your number: "))
    if guessNum < num:
      print("小了")
    elif guessNum > num:
      print("大了")
    else:
      print("猜对了")
      break
  else:
    print("答案是:{}".format(num))
    break
    
