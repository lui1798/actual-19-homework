#encoding: utf-8
from random import randint

init_num = randint(0, 100)
n = 0
k = 0

while n <= 6:
    num = int(input('please input the number you guess:'))
    n += 1
    if num == init_num:
        print('\033[32mCongratulation, you are right!~ \033[0m')
        k = 1
        break
    elif num > init_num:
        print('\033[33mThe nunber is too large!\nYou still have {} chances!\033[0m'.format(6-n))
    else:
        print('\033[34mThe nunber is too small!\nYou still have {} chances!\033[0m'.format(6-n))

if k == 0:
    print('\033[31mSorry, You have failed in the challenge!\nThe random number is \033[0m{}'.format(init_num))
