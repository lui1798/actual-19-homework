#!/usr/bin/emv python
# -*- coding:utf-8 -*-
# author emmby,2018-08-06
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print("\t%d * %d = %d " % (i,j,i*j),end='')
        i += 1
    print("")
    j += 1
print("another way")
for j in range(1,10):
    for i in range(1,j+1):
        print("\t%d * %d = %d " % (i,j,i * j),end='')
    print("")