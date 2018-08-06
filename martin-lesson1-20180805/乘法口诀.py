#coding:gbk

for i in range(1,10):
    for j in range(1,i+1):
        sw = i * j
        
        print('{} * {} = {}'.format(j,i,sw),end=' ')
    print(' ')