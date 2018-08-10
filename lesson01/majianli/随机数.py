# coding:utf-8

import  random
number = 0
inter = random.randint(0,100)

while number <= 5:
    new_number = int(input('输入数字：'))
    if new_number > inter:
        print('大了')
    elif new_number < inter:
        print ('小了')
    else:
        print('对了')
    number +=1



	

	
	

import  random
inter = random.randint(0,100)
for i in range(6):
    new_number = int(input('输入数字：'))
    if new_number > inter:
        print('大了')
    elif new_number < inter:
        print ('小了')
    else:
        print('对了')
