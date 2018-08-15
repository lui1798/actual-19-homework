'''
使用冒泡法对序列[3, 7, 2, 5, 20, 11] 进行排序
auther:gin
'''

l = [3, 7, 2, 5, 20, 11]
t = 0
print("排序前为：{}".format(l))
for x in range(len(l)):
    for y in range(x + 1, len(l)):
        if l[x] > l[y]:
            t = l[x]
            l[x] = l[y]
            l[y] = t
print("排序后为：{}".format(l))
