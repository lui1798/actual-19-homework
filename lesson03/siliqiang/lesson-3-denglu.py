#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : taurusslq
# @Time    : 2018/8/14 下午9:18
# @File    : lesson-3.py
# @Software: PyCharm


import json
import datetime
from prettytable import PrettyTable

"""从文件中读入用户信息"""
userinfo = open("userlistinfo.txt", "r")
userdata = userinfo.read()
usernewlist = json.loads(userdata)
userinfo.close()

userattr = ['id','name','age','tel','address']
# usernewlist = []
#
# userlist = []
# with open("userlistinfo.txt","r",encoding="utf-8") as userinfo:
#     for line in userinfo:
#       userlist.append(line.strip("\n").split(","))
# for i in range(len(userlist)):
#     n = 0
#     userdict = {}
#     while n < 5:
#         userdict[userattr[n]]=userlist[i][n]
#         n += 1
#     usernewlist.append(userdict)
# json_list = json.dumps(usernewlist, indent=1);
# print(json_list)


"""管理员账号密码"""
adminuser = ('admin', 'password')
# username  = input("Please input administrator account: ")
# password  = input("Please input password:")

retry = 0
Flagexit = False

while retry < 3:
    if Flagexit == True:
        break

    """判断管理员账号是否锁定"""
    username = input("Please input administrator account: ")
    password = input("Please input password:")

    """记录账号锁定时间"""
    with open("timeinfo.txt", "r") as time_time:
        logtime = time_time.read()

    time_log = datetime.datetime.strptime(logtime, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(days=1)
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_now_change = datetime.datetime.strptime(time_now, "%Y-%m-%d %H:%M:%S")

    if  time_log > time_now_change:
        lockstr = "Sorry.Your account has been locked! Please try again after 24 hours!"
        print("\033[31m{}\033[0m".format(lockstr.center(50, '*')))
        break

    """验证管理员账号密码,打印成功登陆信息"""
    if username.strip() == adminuser[0] and password.strip() == str(adminuser[1]):
        welcomestr = ["Welcome to User Managent System!!", "Login Success", "Congratulation!!"]
        for i in range(3):
            print("\033[32m{}\033[0m".format(str(welcomestr[i]).center(50, '*')))

        """输入管理员的操作"""
        while True:

            """列出管理员可执行的操作选项"""
            print("\033[36m You can do some operations:\033[0m\n"
                  "L or l  ---> List all users'information\n"
                  "A or a  ---> Add a user\n"
                  "D or d  ---> Delete a user \n"
                  "U or u  ---> Update a user information\n"
                  "F or f  ---> Find a user\n"
                  "E or e  ---> Exit system")
            op = input("Please input your action:")

            """计算分页数量"""
            usernewlistnum = len(usernewlist)

            if usernewlistnum % 5 == 0:
                page = usernewlistnum // 5
            else:
                page = usernewlistnum // 5 + 1

            page_change = 1
            page_row = 0
            flag = False

            """管理员对用户操作"""

            """分页列出用户信息"""
            if op.upper() == 'L':
                while True:
                    if flag == True:
                        break

                    userexcel = PrettyTable(["ID", "NAME", "AGE", "TEL", "ADDRESS"])
                    if page_change == 1:
                        for i in usernewlist[0:5]:
                            userexcel.add_row(i.values())
                        print(userexcel)
                        while True:
                            pagenext = input("Please input 'P' or 'p' (Previous Page),'N' or 'n'(Next PAge),'Q' or 'q'(Quit): ")
                            if pagenext.upper() == 'P':
                                if page_change == 1:
                                    print("\033[031m{}\033[0m".format("This is first page now!".center(50, '*')))
                                else:
                                    page_change -= 1
                                    userexcel = PrettyTable(["ID", "NAME", "AGE", "TEL", "ADDRESS"])
                                    for i in usernewlist[5 * (page_change - 1):5 * page_change]:
                                        userexcel.add_row(i.values())
                                    print(userexcel)
                            elif pagenext.upper() == 'N':
                                if page_change == page:
                                    print("\033[031m{}\033[0m".format("This is last page now!".center(50, '*')))
                                else:
                                    page_change += 1
                                    userexcel = PrettyTable(["ID", "NAME", "AGE", "TEL", "ADDRESS"])
                                    for i in usernewlist[5 * (page_change - 1):5 * page_change]:
                                        userexcel.add_row(i.values())
                                    print(userexcel)
                            elif pagenext.upper() == 'Q':
                                flag = True
                                break
                            else:
                                print("\033[31m{}\033[0m".format("Invalid option! Exit!!".center(50, '*')))
                                flag = True
                                break

                """添加用户"""
            elif op.upper() == 'A':
                try:
                    newuserinfo = input("Please input new user info format like \033[34m'name,age,tel,address'\033[0m:")

                    usernewadd = newuserinfo.split(",")
                    lastid = str(int(usernewlist[len(usernewlist) - 1].get('id')) + 1)

                    k = 1
                    usernewinfo = {}
                    usernewinfo[userattr[0]] = lastid

                    while k < 5:
                        usernewinfo[userattr[k]] = usernewadd[k - 1]
                        # input()
                        # print(usernewinfo)
                        k += 1
                    usernewlist.append(usernewinfo)
                    print("\033[32m{}\033[0m".format("Add new user success".center(50, '*')))
                except:
                    print("\033[31m{}\033[0m".format("Input illegal character!".center(50, '*')))
                    continue

                """更新用户信息"""
            elif op.upper() == 'U':
                updateid = input("Please input your want to update user ID: ")
                updatexcel = PrettyTable(["ID", "NAME", "AGE", "TEL", "ADDRESS"])
                useridlist = []

                for j in range(len(usernewlist)):
                    useridlist.append(usernewlist[j].get('id'))


                if updateid in useridlist:
                    updatexcel.add_row(usernewlist[useridlist.index(updateid)].values())
                    print(updatexcel)
                else:
                    print("\033[31m{}\033[0m".format("Sorry,not found user ID".center(50, '*')))
                    continue

                newartt = input("Please input your want to update attributes:(name,age,tel or address):")
                if newartt not in ['name', 'age', 'tel', 'address']:
                    print("\033[31m{}\033[0m".format("Invilad attributes!".center(50, '*')))
                    continue

                newarttinfo = input("Please input new {}: ".format(newartt))

                usernewlist[useridlist.index(updateid)][newartt] = newarttinfo
                print("\033[32m{}\033[0m".format("Update user success".center(50, '*')))


                """删除用户信息"""
            elif op.upper() == 'D':
                deleteid = input("Please input your want to delete user ID: ")
                deleteexcel = PrettyTable(["ID", "NAME", "AGE", "TEL", "ADDRESS"])
                deleteidlist = []

                for j in range(len(usernewlist)):
                    deleteidlist.append(usernewlist[j].get('id'))

                if deleteid in deleteidlist:
                    l = 0
                    while True:
                        if deleteid == deleteidlist[l]:
                            break
                        l += 1

                    deleteexcel.add_row(usernewlist[l].values())
                    print(deleteexcel)
                    answer = input("Do you sure want to delete this user:(Y/N)")
                    if answer.upper() == 'Y':
                        usernewlist.pop(l)
                        print("\033[32m{}\033[0m".format("Delete user success".center(50, '*')))
                    elif answer.upper() == 'N':
                        print("\033[34m{}\033[0m".format("OK! we will exit!".center(50, '*')))
                        continue
                    else:
                        print("\033[31m{}\033[0m".format("Invilad options!".center(50, '*')))
                        continue
                else:
                    print("\033[31m{}\033[0m".format("Sorry,not found user ID".center(50, '*')))
                    continue

                """查找用户信息"""
            elif op.upper() == 'F':

                findexcel = PrettyTable(["ID", "NAME", "AGE", "TEL", "ADDRESS"])
                f1 = PrettyTable(["ID", "NAME", "AGE", "TEL", "ADDRESS"])
                findlist = []

                findartt = input("Please input your want to find attributes:(id,name,age,tel or address):")
                if findartt not in ['id', 'name', 'age', 'tel', 'address']:
                    print("\033[31m{}\033[0m".format("Invilad attributes!".center(50, '*')))
                    continue

                findarttinfo = input("Please input {} info: ".format(findartt))

                userinfolist=[]
                for g in range(len(usernewlist)):
                    userinfolist.append(usernewlist[g].get(findartt))

                # print(userinfolist)
                if findarttinfo in userinfolist:
                    for k in range(len(usernewlist)):
                        if findarttinfo == usernewlist[k].get(findartt):
                            findexcel.add_row(usernewlist[k].values())
                    print(findexcel)
                else:
                    print("\033[31m{}\033[0m".format("Sorry,not found user info".center(50, '*')))

                """退出系统"""
            elif op.upper() == 'E':
                print("\033[31m{}\033[0m".format("Log out!".center(50, '*')))
                Flagexit = True
                break
            else:
                print("\033[31m{}\033[0m".format("Invalid cmd".center(50, '*')))
                continue

        """写入文本"""
        userlastinfo = open("userlistinfo.txt", "w")
        lastchange = json.dumps(usernewlist, indent=2)
        userlastinfo.write(lastchange)
        userlastinfo.close()

        """判断记录管理员登录尝试次数和时间"""
    else:
        retry += 1
        if retry < 3:
            print("\033[31m{}\033[0m".format("Wrong Username or Password! Try again!".center(50, '*')))
        elif retry == 3:
            with open("timeinfo.txt", "w") as lock_time:
                cur = datetime.datetime.now()
                lock_time.write(cur.strftime("%Y-%m-%d %H:%M:%S"))
                print("\033[31m{}\033[0m".format("You just have three chances.Your account has been locked! Try again after 24 hours!"))
                Flagexit = True

