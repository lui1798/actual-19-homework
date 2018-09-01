import json
import time

'''
 本次修改实现功能：
 1.使用函數實現用戶處理功能

 未实现功能：分页
'''

loginInfo = ['admin', '51reboot']

'''
记录是否还可以进行登录操作
'''

active = True

'''
Lock time is 60 seconds.
'''

LOCK_TIME = 60


def login():
    count = 3
    print("You only have 3 chances today.")
    while count > 0:
        # 判断是否登录成功，如果登录成功，不再进行登录操作
        username = input("please input username: ")
        password = input("please input password: ")
        username = username.strip()
        password = password.strip()
        count -= 1
        if username == loginInfo[0] and password == loginInfo[1]:
            print("\033[32mwelcome! {} \033[0m".format(username))
            return True
        else:
            print("you have %s chance(s)" % count)
    login_lock()
    print("lockd user！")
    return False


def login_lock():
    # 锁定用户
    loginTime = time.time()
    ff = open("locktime.txt", "w")
    ff.write(json.dumps(loginTime))
    ff.close()


def check_lock():
    # 锁定用户
    ff = open("locktime.txt", "r")
    membu = ff.read()
    print(membu)
    unlock_time = float(json.loads(membu)) + LOCK_TIME
    ff.close()
    if time.time() > unlock_time:
        return True
    else:
        return False


def load_userinfo():
    # 加载用户信息
    try:
        fd = open('userInfo.txt', 'r')
        mambaUstring = fd.read()
        fd.close()
        if mambaUstring != '':
            return json.loads(mambaUstring)
    except FileNotFoundError:  # 找不到文件定义空列表。
        return []


def add_user(userList):
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


def list_user(userList):
    for infolist in userList:
        print(infolist)


def delete_user(userList):
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


def update_user(userList):
    modify = input("please input what you want modify(id type(name/age/telNumber/address) value): ")
    updateInfo = modify.split(' ')
    if len(updateInfo) == 3:
        uid = int(updateInfo[0])
        elementType = updateInfo[1]
        value = updateInfo[2]
        if uid in [x['userId'] for x in userList]:
            index = [x['userId'] for x in userList].index(uid)
            oldInfo = userList[index]
            if elementType == 'age':
                value = int(value)
            if elementType in ['name', 'age', 'telNumber', 'address']:
                oldInfo[elementType] = value
                json.dump(userList, open('userInfo.txt', 'w'))

                print("update successful, please check it by list.")
            else:
                print("the type you input is invalid.")
        else:
            print("the id you input is not exist.")


def find_user(userList):
    keyword = input("please input the keyword(userId/name/age/telNumber/address): ")
    exist = False
    for userInfo in userList:
        if (keyword in [userInfo[x] for x in userInfo]) | (
                    int(keyword) in [userInfo[x] for x in userInfo]):
            exist = True
            print(userInfo, end='\n')
    if not exist:
        print("the user you found is not exist.")


def user_main():
    if check_lock():
        if login():
            print("\033[31m----------------------login successful------------------------\033[0m")
        else:
            login_lock()
            exit()
    else:
        print("user is locked, please try again later！")
        exit()
    while True:
        userList = load_userinfo()
        op = input("\033[32minput your operations(add/del/update/list/find/exit): \033[0m")
        if op == "add":
            add_user(userList)
        elif op == "del":
            delete_user(userList)
        elif op == "update":
            update_user(userList)
        elif op == "list":
            list_user(userList)
        elif op == "find":
            find_user(userList)
        elif op == "exit":
            json.dump(userList, open('userInfo.txt', 'w'))
            print("\033[31m--------------------logout------------------------\033[0m")
            exit()
        else:
            print("invalid input！")


user_main()
