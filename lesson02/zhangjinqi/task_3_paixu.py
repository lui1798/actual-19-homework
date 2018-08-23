arr = [3,7,2,5,20,11]
for o in range(len(arr)-1):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
print(arr)
















