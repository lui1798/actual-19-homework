import pickle
import time

userinfo = list([
{'id': 1, 'name': 'name1', 'age': 20, 'tel': '132xxx', 'address': 'beijing'},
{'id': 2, 'name': 'name2', 'age': 20, 'tel': '132xxx', 'address': 'beijing'},
{'id': 3, 'name': 'name3', 'age': 20, 'tel': '132xxx', 'address': 'beijing'},
{'id': 5, 'name': 'name4', 'age': 20, 'tel': '132xxx', 'address': 'beijing'},
{'id': 8, 'name': 'name5', 'age': 20, 'tel': '132xxx', 'address': 'beijing'},
{'id': 9, 'name': 'name6', 'age': 20, 'tel': '132xxx', 'address': 'beijing'}
])
print(userinfo,type(userinfo))
for i in userinfo:
    print(i)
d = dict(name='admin', passwd='playbook', count=3, lasttime=1535080972.4686918)
#pickle.dumps(d)
#with open('file','rb') as f:
#    print(pickle.load(f))
with open('file','wb') as f:
    pickle.dump(d,f)
with open('message','wb') as m:
    pickle.dump(userinfo,m)
