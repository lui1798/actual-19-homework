l=['python','java','python','python','go','java']
count=[]
lei =[]
for i in l:
    a=l.count(i)
    lei.append(i)
    count.append(a)
b=dict(zip(lei,count))
print(b)



# fd=open('/etc/passwd')
# a=0
# for line in fd:
#     # print (line[-6:])
#     if  line[-6:].strip() == 'false':
#         a+=1
# print (a)
# fd.close()