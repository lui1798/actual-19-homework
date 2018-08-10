import random
x = random.randint(1,100)

print ('You have 6 chances to guess numbers,Please input:')
for i in range(6):
    r = int(input())
    if r>x:
        print ('too large')
    elif r<x:
        print ('too small')
    else:
        print ('Congratulations')
        break
print ('game over')