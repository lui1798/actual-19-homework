#!/bin/python
arr = [9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9]
for i in range(len(arr)-1):
  for j in range(len(arr)-1-i):
    if arr[j] > arr [j+1]:
      arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr)
