#!/usr/bin/env python
for i in range(1,10):
    for x in range(1,i+1):
        print('{} * {} = {} '.format(x, i, i*x),end='')
    print()