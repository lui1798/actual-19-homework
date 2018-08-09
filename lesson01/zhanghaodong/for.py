#!/usr/bin/python
# mail:haodongz@yeah.net
# _*_ coding:utf-8 _*_ 

for i in range(1, 10):
    for j in range(1, i+1):
        print("%d*%d=%d\t" % (i, j, i*j), end="")
    print()
