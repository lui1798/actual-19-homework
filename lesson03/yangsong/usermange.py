# -*- coding: utf-8 -*-
import json, datetime, os
#参数定义：
admininfo = ('admin', 'admin123')
count = 0
flag = 0
userinfo = []
while count < 3 and flag == 0:
    username = input("Please input your username: ")
    passwd = input("Please input your passwd: ")
    if username == admininfo[0] and passwd == admininfo[1]:
        print("Welcome!")
        while True:
            op = input("Please input your operation(add/delete/update/list/find/write/exit): ")
            if op == "add":
                information = input("Please input your information(name tel address age , ex: ys 18812345678 jiangsu 22): ")
                user_list = information.split(' ')
                if len(user_list) < 4:
                    print("Please try again: ")
                elif len(user_list) == 4:
                    if len(userinfo) == 0:
                        user_list.insert(0, '1')
                        userinfo.append(user_list)
                        print(userinfo)
                    else:
                        uid = len(userinfo)
                        auid = uid + 1
                        user_list.insert(0, str(auid))
                        userinfo.append(user_list)
                    print("{} \n add successly")
                else:
                    print("Try again")
            elif op == "delete":
                duid = input("Please input your id: ")
                for duid in userinfo:
                    userinfo.remove(duid)
                    print('Delete {} successly'.format(duid))
                for item in userinfo:
                    print(item)
                else:
                    print("Try again")
            elif op == "update":
                information = input("Please input your updated information(ex: 2 tel ): ")
                user_update = information.split(' ')
                if len(user_update) == 3:
                    if user_update[0] in [x['seq'] for x in userinfo]:
                        for(i, y) in enumerate(userinfo):
                            if user_update[0] == y['seq']:
                                if user_update[1] in ['name', 'tel', 'address', 'age']:
                                    userinfo[i][user_update[1]] = user_update[2]
                                else:
                                    print("Nothing to change")
                    else:
                        print("userid not found")
                else:
                    print("information error")
                print(userinfo)
            elif op == list:
                try:
                    page_size = int(input("Please input your page_size"))
                except ValueError:
                    print("ValueError")
                else:
                    if page_size == 0:
                        print("try again")
                    else:
                        page_num = len(userinfo) // page_size +1
                        while True:
                            try:
                                n = int(input("Please input your page num: "))
                            except ValueError:
                                print("ValueError")
                            else:
                                if n in range(1, page_num + 1):
                                    for i in ['UserID', 'name', 'tel', 'address', 'age']:
                                        print("{:<20}".format(i), end=' ')
                                        print('')
                                        for x in userinfo[(n - 1)] * page_size:
                                            for j in x:
                                                print("{:<20}".format(i), end=' ')
                                            print('')
                                    out = input("exit(yes/no):")
                                    if out == 'yes':
                                        break
                                else:
                                    print("nothing found")
            elif op == 'list':
                for item in userinfo:
                    print(item)
            elif op == 'write':
                data_write = json.dumps(userinfo)
                fd = open('persistence.db', 'w')
                fd.write(data_write)
                fd.close()
                print("write successly")
            elif op == "exit":
                fd = open('persistence.db', 'r')
                membuf = fd.read()
                fd.close()
                userinfo_e = json.loads(membuf)
                flag_exit = True
                if userinfo_e != userinfo:
                    op_again = input("really?(y/n)")
                    if op_again == 'n':
                        flag_exit =False
                if flag_exit == True:
                    print("success")
                    break
            else:
                print("nothing")
            continue
        break