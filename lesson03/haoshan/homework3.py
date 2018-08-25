import datetime
import json

'''
 本次修改实现功能：
 1.实现字典功能
 2.实现user数据持久化
 3.异常处理
 4.3次输错密码，超过24小时才可登录

 未实现功能：分页
'''

'''
登录信息：username password
'''
loginInfo = ['admin', '51reboot']

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
    currentTime = datetime.datetime.strptime(str(datetime.datetime.now()).split('.')[0], '%Y-%m-%d %H:%M:%S')
    try:
        currentTime = currentTime + datetime.timedelta(days=-1)
        dsTime = open('time.txt', 'r')
        saveTime = dsTime.read()
        # saveTime = json.loads(saveTime)
        if saveTime != '':
            saveTime = datetime.datetime.strptime(saveTime, '%Y-%m-%d %H:%M:%S')
        else:
            saveTime = currentTime
        dsTime.close()

    except FileNotFoundError:
        saveTime = currentTime
    # 判断今天是否拥有权限登录
    if saveTime <= currentTime:
        count = 3
        login = False
        print("You only have 3 chances today.")
        while count > 0:
            # 判断是否登录成功，如果登录成功，不再进行登录操作
            if not login:
                username = input("please input username: ")
                password = input("please input password: ")
                username = username.strip()
                password = password.strip()
                count -= 1
                if username == loginInfo[0] and password == loginInfo[1]:
                    print("\033[32mwelcome! {} \033[0m".format(username))
                    login = True
                    count = 3
            # 登录成功，进行操作
            if login:
                op = input("\033[32minput your operations(add/del/update/list/find/exit): \033[0m")
                userList = []
                try:
                    fd = open('userInfo.txt', 'r')
                    membufUserinfo = fd.read()
                    if (membufUserinfo != ''):
                        userList = json.loads(membufUserinfo)
                    fd.close()
                except FileNotFoundError:  # 找不到文件定义空列表。
                    userList = []
                print(userList)
                if op == 'add':
                    body = input("input userInfo(name age telNumber address): ")
                    userInfo = body.split(' ')
                    if len(userInfo) != 4:
                        print("invalid input")
                    else:
                        userInfoDic = {'userId': 0, 'name': userInfo[0], 'age': int(userInfo[1]),
                                       'telNumber': userInfo[2], 'address': userInfo[3]}
                        if len(userList) == 0:
                            userInfoDic['userId'] = 1
                        else:
                            uids = [x['userId'] for x in userList]
                            newId = max(uids) + 1
                            userInfoDic['userId'] = newId
                        userList.append(userInfoDic)

                        json.dump(userList, open('userInfo.txt', 'w'))
                        print("your information added successfully!")

                elif op == 'del':
                    print(len(userList))
                    if len(userList) != 0:
                        delInput = int(input("input the userId which you want to delete: "))
                        delId = int(delInput)
                        if delId in [x['userId'] for x in userList]:
                            for x in userList:
                                if x['userId'] == delId:
                                    userList.remove(x)
                                    break
                            json.dump(userList, open('userInfo.txt', 'w'))
                            print("your information deleted successfully!")
                        else:
                            print("invalid input")
                    else:
                        print("the useList is empty,please add information first")

                elif op == 'update':
                    modify = input("please input what you want modify(id type(name/age/telNumber/address) value): ")
                    updateInfo = modify.split(' ')
                    if len(updateInfo) == 3:
                        uid = int(updateInfo[0])
                        type = updateInfo[1]
                        value = updateInfo[2]
                        if uid in [x['userId'] for x in userList]:
                            index = [x['userId'] for x in userList].index(uid)
                            oldInfo = userList[index]
                            if type == 'age':
                                value = int(value)
                            if type in ['name', 'age', 'telNumber', 'address']:
                                oldInfo[type] = value
                                json.dump(userList, open('userInfo.txt', 'w'))

                                print("update successful, please check it by list.")
                            else:
                                print("the type you input is invalid.")
                        else:
                            print("the id you input is not exist.")

                elif op == 'list':
                    for infolist in userList:
                        print(infolist)

                elif op == 'find':
                    keyword = input("please input the keyword(userId/name/age/telNumber/address): ")
                    exist = False
                    for userInfo in userList:
                        if (keyword in [userInfo[x] for x in userInfo]) | (
                            int(keyword) in [userInfo[x] for x in userInfo]):
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
            try:
                df = open('time.txt', 'w')
                df.write(str(currentTime))
                df.close()
            except FileNotFoundError:
                print("time.txt is not exist.")
    else:
        print("Sorry! You have no chance today, please try again tomorrow.")
