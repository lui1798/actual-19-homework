'''
id    username    age    tel    address
1     chenlei     25     158xxx    xx
...
'''

userinfo = []
loginfo = ('admin', 'admin123')
count = 0
flag = 0

while count < 3 and flag == 0:
    username = input('Input username:')
    password = input('Input password:')
    if username == loginfo[0] and password == loginfo[1]:
        print('Log success\nInput op: add/del/change/list/exit')
        while True:
            op = input('Input op:')
            if op == 'add':
                addinfo = input('Input userinfo:')
                userlist = addinfo.split(' ')
                if len(userinfo) == 0:
                    userlist.insert(0, 1)
                    userinfo.append(userlist)
                    print(userinfo)
                else:
                    uids = len(userinfo)
                    newid = uids + 1
                    userlist.insert(0, newid)
                    userinfo.append(userlist)
                    for item in userinfo:
                        print(item)
            elif op == 'del':
                uids = input('Input uid:')
                for id in userinfo:
                    if id[0] == uids:
                        userinfo.remove(id)
                        print('delete uid:%s success' %uids)
                for item in userinfo:
                    print(item)
            elif op == 'change':
                uids = input('Input uid:')

            elif op == 'list':
                for item in userinfo:
                    print(item)
            elif op == 'exit':
                print('Exit...')
                flag = 1
                break
            else:
                print('Invalid input op')
                continue
    else:
        if flag == 1:
            exit(1)
        else:
            count += 1
            if count < 3:
                print('Invalid username or password, %s times left' %(3 - count))
            else:
                print('Log error more than 3 times,exit...')
                break
