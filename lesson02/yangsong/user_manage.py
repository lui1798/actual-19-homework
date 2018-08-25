# -*- coding: utf-8 -*-
#参数定义
admininfo = ['admin','admin']
userinfo = []
count = 0
flag = 0
#登陆判断
while count < 3 and flag == 0:
    username = input("Please input your username : ")
    passwd = input("Please input your passwd: ")
    if username == admininfo[0] and passwd == admininfo[1]:
        print("Success \n please input your operation(add/del/change/list/exit): ")
        while True:
            op = input('Please input your operation: ')
            if op == 'add':
                addinfo = input("Plese input your addinfo(name\t age\t tel\t address\t): ")
                userlist = addinfo.split(' ')
                if len(userlist) == 0:
                    userlist.insert(0,1)
                    userinfo.append(userlist)
                    print(userinfo)
                else:
                    uid = len(userinfo)
                    newuid = uid + 1
                    userlist.insert(0, newuid)
                    userinfo.append(userlist)
                    for item in userinfo:
                        print(item)
            elif op == 'del':
                uids = input("Please input your uid: ")
                for uids in userinfo:
                    userinfo.remove(uids)
                    print('Delete {} successly'.format(uids))
                for item in userinfo:
                    print(item)
            elif op == 'change':
                uid = input("Plese input your uid: ")
            elif op == 'list':
                for item in userinfo:
                    print(item)
            elif op == 'exit':
                print("Exit")
                flag = 1
                break
            else:
                input("Please input right operation")
                continue
    else:
        if flag ==1:
            exit(1)
        else:
            count += 1
            if count < 3:
                print("Please input correct username and passwd")
            else:
                print("exit")
                break






