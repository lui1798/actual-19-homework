#!/usr/bin/python
# mail:haodongz@yeah.net
# _*_ coding:utf-8 _*_ 


username = input("please your name:")
password = int(input("please your password:"))
_user = 'haodongz'
_passwd = 123

d = {}
while True:

    if username == _user and password == _passwd:

        print('welcome to {} '.format(username))
        while True:

            add = input("please you add,up,del，格式name,27")

            if add == 'add':
                '''添加用户信息'''
                usersearch = input("please add  user info:")
                _usersearch = usersearch.strip('')
                arr=_usersearch.split(',')
                d[arr[0]]=dict(name=arr[0],age=arr[1])
                print(d[arr[0]])
            elif add == 'up':
                usersearch = input("please up  user info:")
                _usersearch = usersearch.strip('')
                arr = _usersearch.split(',')
                d[arr[0]] = dict(name=arr[0], age=arr[1])
                print(d[arr[0]])
            elif add == 'del':
                 usersearch = input("please del  user info:")
                 usersearch = usersearch.strip()
                 print(usersearch)
                 print(d)
                 print(len(usersearch))
                 if usersearch == d.get('name'):
                     d.pop('name')
                 elif usersearch == d.get('age'):
                     d.pop('age')
                 else:
                     print('空')

            elif add == 'exit':
                exit()
                print("exit")

        else:
            print("密码错误")
            break

