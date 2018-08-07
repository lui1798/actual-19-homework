#猜数游戏
import random
number = random.randint(1,100)
i = 1
while i <= 6:
    number_input = int(input("请输入猜的数："))

    if number_input > number:
        print ("大了")
    elif number_input < number:
        print ("小了")
    else:
        print ("猜对了")
        break
    i+=1
if i ==7:
    print ("未猜中，游戏结束")

