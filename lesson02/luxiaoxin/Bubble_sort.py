#encoding: utf-8
l = [3, 7, 2, 5, 20, 11]

print('The original list:{0}'.format(l))

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]

print('->The sorted list:{0}'.format(l))