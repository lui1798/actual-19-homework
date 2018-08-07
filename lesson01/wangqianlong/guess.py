import random

value = random.randint(0, 100)
# print(value)
i = 0
while i < 7:
    num = int(input('Please guess a number(<100): '))
    if value == num:
        print('OK,you are right!')
        break
    elif value > num:
        print('Smaller...')
    else:
        print('Larger...')
    i = i + 1
    if i == 6:
        print("You have guessed 6 times and can't guess anymore...")
        break
