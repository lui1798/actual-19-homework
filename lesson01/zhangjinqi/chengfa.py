#观察乘法口诀表的规律：第一列开头是1，第二列开头是2，以此类推。
#每到两数相等时，输出需要换行。补全矩形乘法口诀表，发现多余项都为i比o大，所以只需输出i比o小的项。
#美中不足的是，第三、四排不好对齐。

for o in range(1,10):
    for i in range(1,10):
        s = o * i
        if i == o:
            print('{}*{}={}'.format(i,o,s))
        elif i < o:
            print('{}*{}={}'.format(i,o,s),end=' ')
