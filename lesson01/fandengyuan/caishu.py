import random

nums=random.randint(0,100)
n=0

while n < 6:
    yours = input("please input your num:")
    yours = int(yours)
    if yours == nums:
        print("Congratulations,you get it!!!")
        break
    elif yours < nums:
        print("you should guess bigger!")
    elif yours > nums:
        print("you should guess smaller!")
    n += 1
else:
    print("your chance is over")
