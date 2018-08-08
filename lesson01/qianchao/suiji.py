import random
a=random.randint(1,100)
print(a)
c=1
while c<=6:
    b=int(input('please input num: '))
    c+=1
    if b==a:
        print("恭喜你答对了")
        break
    elif b>a:
        print("大了")
    elif b<a:
        print('小了')
