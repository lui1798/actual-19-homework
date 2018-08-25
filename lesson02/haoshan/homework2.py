import datetime

'''
客户信息：id name age telnum address
'''
userlist = [
    [1, 'monkey1', 21, '131xxx', 'beijing'],
    [2, 'monkey2', 22, '132xxx', 'shanghai'],
    [3, 'monkey3', 23, '133xxx', 'guangzhou'],
    [4, 'monkey4', 24, '134xxx', 'shenzhen'],
    [5, 'monkey5', 25, '135xxx', 'wuhan']
]

'''
登录信息：username password
'''

loginInfo = ['admin', '51reboot']

'''
记录操作时间，用于判断是否可以登录
'''

date = datetime.date.today()

'''
记录是否还可以进行登录操作
'''

active = True

'''
Log in only three times a day.
'''

count = 3

'''
使用无限循环模拟服务器运行环境
'''

while True:

    # 使用键盘操作触发业务
    input()
    # 获取当前日期
    tryDate = datetime.date.today()
    # 判断今天是否拥有权限登录
    if (tryDate >= date) & active:
        date = tryDate
        count = 3
        login = False
        print("You only have three chances today.")
        while count > 0:
            # 判断是否登录成功，如果登录成功，不再进行登录操作
            if not login:
                username = input("please input username: ")
                password = input("please input password: ")
                count -= 1
                if username == loginInfo[0] and password == loginInfo[1]:
                    print("\033[32mwelcome! {} \033[0m".format(username))
                    login = True
            # 登录成功，进行操作
            if login:
                op = input("\033[32minput your operations(add/del/update/list/find/exit): \033[0m")

                if op == 'add':
                    body = input("input userInfo(name age telNumber address): ")
                    userInfo = body.split(' ')
                    if len(userInfo) != 4:
                        print("invalid input")
                    else:
                        userInfo[1] = int(userInfo[1])
                        if len(userlist) == 0:
                            userInfo.insert(0, 1)
                        else:
                            userInfo.insert(0, int(userlist[-1][0]) + 1)
                        userlist.append(userInfo)
                        print("your information added successfully!")

                elif op == 'del':
                    if len(userlist) != 0:
                        delInput = int(input("input the userid which you want to delete: "))
                        if delInput in [x[0] for x in userlist]:
                            userlist.remove(delInput)
                            print("your information deleted successfully!")
                        else:
                            print("invalid input")
                    else:
                        print("the uselist is empty,please add information first")

                elif op == 'update':
                    modify = input("please input what you want modify(id type(1:name/2:age/3:tel/4:addr) value): ")
                    updateInfo = modify.split(' ')
                    if len(updateInfo) == 3:
                        uid = int(updateInfo[0])
                        type = int(updateInfo[1])
                        value = updateInfo[2]
                        if uid in [x[0] for x in userlist]:
                            index = [x[0] for x in userlist].index(uid)
                            oldInfo = userlist[index]
                            if type == 2:
                                value = int(value)
                            if type in range(1, 5):
                                oldInfo[type] = value
                                print("update successful, please check it by list.")
                            else:
                                print("the type you input is invalid.")
                        else:
                            print("the id you input is not exist.")

                elif op == 'list':
                    for infolist in userlist:
                        print(infolist)

                elif op == 'find':
                    keyword = input("please input the keyword(id/name/age/tel/address): ")
                    exist = False
                    for userInfo in userlist:
                        if (keyword in userInfo) | (int(keyword) in userInfo):
                            exist = True
                            print(userInfo, end='\n')
                    if not exist:
                        print("the user you found is not exist.")

                elif op == 'exit':
                    print("logout")
                    break

                else:
                    print("invalid input")

            else:
                print("you have %s chance(s)" % count)
        # 判断今天是否还有登录次数，如果没有则active=false，不允许进行操作
        if count == 0:
            print("Sorry, please try again tomorrow.")
            active = False
    else:
        print("Sorry! You have no chance today, please try again tomorrow.")
