#
# 1*1=1
# 1*2=2 2*2=4
# 1*3=3 2*3=6 3*3=9
# .....
# 1*9=9 2*9=18 3*9=27 4*9=36 5*9=45 6*9=54 7*9=63 8*9=72 9*9=81
#
for i in range(1, 10):
    for j in range(1, i + 1):
        if i * j < 10:
            ij = str(i * j) + ' '
        else:
            ij = i * j
        if i == j:
            print('{} * {} = {}  '.format(j, i, ij))
        else:
            print('{} * {} = {} '.format(j, i, ij), end=' ')
