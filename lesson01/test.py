l=['python','java','python','python','go','java']
count=[]
lei =[]
for i in l:
    a=l.count(i)
    lei.append(i)
    count.append(a)
b=dict(zip(lei,count))
print(b)
print(dict(zip(lei,count)))
