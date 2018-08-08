#!/usr/bin/env python3
for i in range(1,10):
     for j in  range(1,i+1):
          x = i * j
          if j == i:
              print("{}*{}={}  \n".format(j,i,x),end='')
          else:
              print("{}*{}={}  ".format(j,i,x),end='')
          j += 1
     i += 1


