#!/usr/bin/env python
# -*- coding:utf-8 -*-

n = 1
m = 1
j = 1

while j < 10:
    j += 1
    while n < j:
        print ("{} x {} = {}".format(n,m,m*n),end=" ")
        n += 1
    print()
    m += 1
    n = 1








