#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : taurusslq
# @Time    : 2018/8/14 下午9:18
# @File    : lesson-2.py
# @Software: PyCharm

import math
from prettytable import PrettyTable


"""用户信息转换成列表"""
userlist = []
with open("userlistinfo.txt","r",encoding="utf-8") as userinfo:
    for line in userinfo:
      userlist.append(line.strip("\n").split(","))



"""管理员账号密码"""
adminuser = ('admin','password')
username  = input("Please input adminaccount: ")
password  = input("Please input password:")


"""验证管理员账号密码,打印成功登陆信息"""
if username == adminuser[0] and password == adminuser[1]:
    welstr = ["Welcome to User Managent System!!","Login Success","Congratulation!!"]
    for i in range(3):
        print("\033[32m{}\033[0m".format(str(welstr[i]).center(50,'*')))


    """输入管理员的操作"""
    Pagechange = 'No'
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
        usernum = len(userlist)
        page = math.ceil(usernum / 5)
        if op.upper()=='L':
            n = 1
            while True:
                userexcel = PrettyTable(["ID", "NAME", "AGE", "TEL", "ADDRESS"])
                if n == page:
                    for i in range(5 * (n - 1), usernum):
                        userexcel.add_row(userlist[i])
                    print(userexcel)
                elif n < page:
                    for i in range(5 * (n - 1), 5 * n):
                        userexcel.add_row(userlist[i])
                    print(userexcel)
                Pagechange = input("Please input 'P' or 'p' (Previous Page),'N' or 'n'(Next PAge),'Q' or 'q'(Quit): ")

                if Pagechange.upper() == 'P':
                    n -= 1
                elif Pagechange.upper() == 'N':
                    n += 1
                elif Pagechange.upper() == 'Q':
                        break
                else:
                    print("\033[31m{}\033[0m".format("Invalid option".center(50, '*')))
                    break

            """添加用户"""
        elif op.upper() == 'A':
            newuserinfo = input("Please input newuser format like \033[34m'name,age,tel,address'\033[0m:")
            lastid = str(int(userlist[len(userlist)-1][0]) + 1)
            newuseradd = lastid + ',' + newuserinfo
            userlist.append(newuseradd.split(","))
            print("\033[32m{}\033[0m".format("Add newuser success".center(50, '*')))

            """更新用户信息"""
        elif op.upper() == 'U':
            updateid = input("Please input your want to update user ID: ")
            updatexcel = PrettyTable(["ID", "NAME", "AGE", "TEL", "ADDRESS"])
            useridlist = []

            for j in range(len(userlist)):
                useridlist.append(userlist[j][0])

            if updateid in useridlist:
                updatexcel.add_row(userlist[int(updateid)-1])
                print(updatexcel)
            else:
                print("\033[31m{}\033[0m".format("Sorry,not found user ID".center(50, '*')))
                continue

            newartt = input("Please input your want to update attributes:(name,age,tel or address):")
            if newartt not in ['name','age','tel','address']:
                print("\033[31m{}\033[0m".format("Invilad attributes!".center(50, '*')))
                continue

            newarttinfo = input("Please input new {}: ".format(newartt))
            if newartt == 'name':
                userlist[int(updateid)-1][1] = newarttinfo
            elif newartt == 'age':
                userlist[int(updateid)-1][2] = newarttinfo
            elif newartt == 'tel':
                userlist[int(updateid)-1][3] = newarttinfo
            elif newartt == 'address':
                userlist[int(updateid)-1][4] = newarttinfo


            """删除用户信息"""
        elif op.upper() == 'D':
            deleteid = input("Please input your want to delete user ID: ")
            deleteexcel = PrettyTable(["ID", "NAME", "AGE", "TEL", "ADDRESS"])
            deleteidlist = []

            for j in range(len(userlist)):
                deleteidlist.append(userlist[j][0])

            if deleteid in deleteidlist:
                deleteexcel.add_row(userlist[int(deleteid)-1])
                print(deleteexcel)
                answer = input("Do you sure want to delete this user:(Y/N)")
                if answer.upper() == 'Y':
                    userlist.pop(int(deleteid)-1)
                    print("\033[32m{}\033[0m".format("Delete user success".center(50, '*')))
                elif answer.upper() == 'N':
                    print("OK! we will exit!")
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
            findlist = []
            findartt = input("Please input your want to find attributes:(id,name,age,tel or address):")
            if findartt not in ['id','name', 'age', 'tel', 'address']:
                print("\033[31m{}\033[0m".format("Invilad attributes!".center(50, '*')))
                continue

            findarttinfo = input("Please input {} info: ".format(findartt))

            if findartt == 'id':
                for k in range(len(userlist)):
                    if findarttinfo == userlist[k][0]:
                        findexcel.add_row(userlist[k])
                print(findexcel)
            elif findartt == 'name':
                for k in range(len(userlist)):
                    if findarttinfo == userlist[k][1]:
                        findexcel.add_row(userlist[k])
                print(findexcel)
            elif findartt == 'age':
                for k in range(len(userlist)):
                    if findarttinfo == userlist[k][2]:
                        findexcel.add_row(userlist[k])
                print(findexcel)
            elif findartt == 'tel':
                for k in range(len(userlist)):
                    if findarttinfo == userlist[k][3]:
                        findexcel.add_row(userlist[k])
                print(findexcel)
            elif findartt == 'address':
                for k in range(len(userlist)):
                    if findarttinfo == userlist[k][4]:
                        findexcel.add_row(userlist[k])
                print(findexcel)
            else:
                print("\033[31m{}\033[0m".format("Sorry,not found user ID".center(50, '*')))
                continue

            """退出系统"""
        elif op.upper() == 'E':
            print("\033[31m{}\033[0m".format("Log out!".center(50, '*')))
            break
        else:
            print("\033[31m{}\033[0m".format("Invalid cmdD".center(50, '*')))
            continue

    with open("userlistinfo.txt", "w") as out_file:
            for o in range(len(userlist)):
                for p in range(5):
                    if p == 4:
                        out_file.write(userlist[o][p])
                    else:
                        out_file.write(userlist[o][p] + ",")
                out_file.write("\n")

else:
    print("\033[31m{}\033[0m".format("Incorrect username or password,Login failed!".center(50, '*')))

