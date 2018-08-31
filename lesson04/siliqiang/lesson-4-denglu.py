#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : taurusslq
# @Time    : 2018/8/26
# @File    : lesson-4.py
# @Software: PyCharm


import json
import time
import math
import getpass
from prettytable import PrettyTable


'''
设置常量
'''
lock_file = "locktime"
lock_duration = 60 * 60 * 24
max_login_times = 3
userinfo_num = 4
has_error = True
is_exists = False

'''
管理员用户名，密码
'''
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

'''
判断是否锁定
'''
def is_unlock():
    lock_time = 0

    try:
        locktime_file = open(lock_file,"r")
        hander = locktime_file.read()
        locktime_file.close()
        lock_time = float(hander)
    except Exception as e:
        pass

    return time.time() - lock_time > lock_duration

'''
写入锁定时间
'''
def is_lock():
    lockwritetime = open(lock_file, 'w')
    lockwritetime.write(str(time.time()))
    lockwritetime.close()

'''
显示登录信息
'''
def login():
    is_login = False

    for i in range(max_login_times):
        username = input("Please input administrator account: ")
        password = getpass.getpass("Please input password:")

        if ADMIN_USERNAME == username and ADMIN_PASSWORD == password:
            is_login = True
            break

        if max_login_times - 1 == i:
            lockstr = "Sorry.Your account has been locked! Please try again after 24 hours!"
            print("\033[31m{}\033[0m".format(lockstr.center(50, '*')))
        else:
            print("\033[31m{}\033[0m".format("You just have three chances,Please try again!"))

    return is_login

'''
输出锁定信息
'''
def lock_login():
    print("\033[31m{}\033[0m".format("Sorry.Your account has been locked! Please try again after 24 hours!"))

'''
读取用户信息
'''
def get_users():
    userlist = []

    try:
        listuser = open("user.txt", "r")
        userdata = listuser.read()
        userlist = json.loads(userdata)
        listuser.close()
    except FileNotFoundError:
        pass

    return userlist

'''
分页打印用户信息
'''
def list_users(userlist):
    page = math.ceil(len(userlist) / 5)
    while True:
        userexcel = PrettyTable(["ID", "NAME", "AGE", "TEL", "ADDRESS"])
        input_page_num = input("Total {0} pages，Please input you want page 1~{0},(input 'Q' or 'q' quit.): ".format(page))
        if input_page_num.isdigit() and 0 < int(input_page_num) <= page:
            page_num = int(input_page_num)
            for i in userlist[5 * (page_num - 1):5 * page_num]:
                userexcel.add_row(i.values())
            print(userexcel)
        elif input_page_num.upper() == "Q":
            break
        else:
            print("\033[31m{}\033[0m".format("Input wrong page number!".center(50, '*')))
            break

'''
添加用户信息
'''
def add_users(userlist):
    newuserinfo = input("Please input new user info format like \033[34m'name,age,tel,address'\033[0m:")
    newuser = newuserinfo.split(",")
    has_error = True

    while has_error:

        has_error = False
        if len(newuser) != userinfo_num:
            newuserinfo = input("User info has something wrong,Please input again:")
            newuser = newuserinfo.split(",")
            has_error = True
        else:
            name, age, tel, address = newuser

            if not age.isdigit():
                print("\033[31m{}\033[0m".format("Input wrong age!".center(50, '*')))
                print(newuser)
                newuserinfo = input("User info has something wrong,Please input again:")
                newuser = newuserinfo.split(",")
                has_error = True

            elif not tel.isdigit():
                print("\033[31m{}\033[0m".format("Input wrong tel number!".center(50, '*')))
                newuserinfo = input("User info has something wrong,Please input again:")
                newuser = newuserinfo.split(",")
                has_error = True

            if not has_error:
                maxid = max([x.get('id') for x in userlist] + [0]) + 1
                userlist.append({
                    'id': maxid,
                    'name': name,
                    'age': int(age),
                    'tel': tel,
                    'address': address
                })
                print("\033[32m{}\033[0m".format("Add new user success".center(50, '*')))

    return  userlist

'''
删除用户
'''
def del_users(userlist):
    deleteid = input("Please input your want to delete user ID: ")
    deleteexcel = PrettyTable(["ID", "NAME", "AGE", "TEL", "ADDRESS"])
    deleteidlist = []

    if deleteid.isdigit():
        uid = int(deleteid)
        for user in userlist:
            if uid == user.get("id"):
                deleteexcel.add_row(user.values())
                print(deleteexcel)
                answer = input("Do you sure want to delete this user:(Y/N)")

                if answer.upper() == 'Y':
                    userlist.remove(user)
                    print("\033[32m{}\033[0m".format("Delete user success".center(50, '*')))
                    break
                elif answer.upper() == 'N':
                    print("\033[34m{}\033[0m".format("OK! we will exit!".center(50, '*')))
                    break
                else:
                    print("\033[31m{}\033[0m".format("Invilad options!".center(50, '*')))
        else:
            print("\033[31m{}\033[0m".format("Input wrong ID".center(50, '*')))
    else:
        print("\033[31m{}\033[0m".format("Sorry,not found user ID".center(50, '*')))

    return userlist

'''
更新用户信息
'''
def update_users(userlist):
    updateid = input("Please input your want to update user ID: ")
    updatexcel = PrettyTable(["ID", "NAME", "AGE", "TEL", "ADDRESS"])
    updateuser = []

    if updateid.isdigit():
        uid = int(updateid)
        for user in userlist:
            if uid == user.get('id'):
                updateuser = user
                updatexcel.add_row(user.values())
                print(updatexcel)
                is_exists = True
                break
    else:
        print("\033[31m{}\033[0m".format("Sorry,not found user ID".center(50, '*')))

    if is_exists:
        newartt = input("Please input your want to update attributes:(name,age,tel or address):")
        if newartt not in ['name', 'age', 'tel', 'address']:
            print("\033[31m{}\033[0m".format("Invilad attributes!".center(50, '*')))

        else:
            newarttinfo = input("Please input new {}: ".format(newartt))

            if newartt == 'age' or newartt == 'tel':
                if newarttinfo.isdigit():
                    updateuser[newartt] = newarttinfo
                else:
                    print("\033[31m{}{}\033[0m".center(50, '*').format("Input wrong ", newartt))
            else:
                updateuser[newartt] = newarttinfo
                print("\033[32m{}\033[0m".format("Update user success".center(50, '*')))

    return userlist

'''
查找用户
'''
def find_users(userlist):
    findexcel = PrettyTable(["ID", "NAME", "AGE", "TEL", "ADDRESS"])
    findartt = input("Please input your want to find user info(ID,NAME,AGE,TEL OR ADDRESS):")
    find_flag = False

    for user in userlist:
        if str(user.get("id"))== findartt or \
           user.get("name") == findartt or \
           str(user.get("age")) == findartt or \
           user.get("tel") == findartt or \
           user.get("address") == findartt:
            findexcel.add_row(user.values())
            find_flag = True

    if find_flag:
        print(findexcel)

    if not find_flag:
        print("\033[31m{}\033[0m".format("Input wrong user info".center(50, '*')))

'''
退出系统，保存用户信息
'''
def exit_users(userlist):
    print("\033[31m{}\033[0m".format("Log out!".center(50, '*')))
    userlastinfo = open("user.txt", "w")
    lastchange = json.dumps(userlist, indent=2)
    userlastinfo.write(lastchange)
    userlastinfo.close()
    exit()

'''
管理员操作
'''
def op_users(userlist):
        welcomestr = ["Welcome to User Managent System!!", "Login Success", "Congratulation!!"]
        for i in range(3):
            print("\033[32m{}\033[0m".format(str(welcomestr[i]).center(50, '*')))

        '''
        登录成功后输入操作
        '''
        while True:

            '''
            列出管理员可执行的操作选项
            '''
            print("\033[36m You can do some operations:\033[0m\n"  
                    "L or l  ---> List all users'information\n"      
                    "A or a  ---> Add a user\n"                      
                    "D or d  ---> Delete a user \n"                  
                    "U or u  ---> Update a user information\n"       
                    "F or f  ---> Find a user\n"                     
                    "E or e  ---> Exit system")
            op = input("Please input your action:")

            if op.upper() == 'L':
                list_users(userlist)
            elif op.upper() == 'A':
                userlist = add_users(userlist)
            elif op.upper() == 'D':
                userlist = del_users(userlist)
            elif op.upper() == 'U':
                userlist = update_users(userlist)
            elif op.upper() == 'F':
                find_users(userlist)
            elif op.upper() == 'E':
                exit_users(userlist)
            else:
                print("\033[31m{}\033[0m".format("Invalid cmd".center(50, '*')))
'''
主函数
'''
def main():
    if not is_unlock():
        lock_login()
        return
    if login():
        userlist = get_users()
        op_users(userlist)
    else:
        is_lock()

main()