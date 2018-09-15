#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : taurusslq
# @Time    : 2018/9/11 上午12:06
# @File    : moduleop.py
# @Software: PyCharm

import math
import logging
import xlwt
from prettytable import PrettyTable
from modulemysql import add_user_mysql
from modulemysql import user_id_mysql
from modulemysql import list_user_mysql
from modulemysql import find_user_mysql
from modulemysql import del_user_mysql
from modulemysql import update_user_mysql
from modulefile import ReadConfig


'''
设置变量
'''

userinfo_num = 4
has_error = True

'''
分页打印用户信息
'''
def list_users():
    userlist = list_user_mysql()
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
def add_users():
    newuserinfo = input("Please input new user info format like \033[34m'name,age,tel,address'\033[0m:")
    newuser = newuserinfo.split(",")
    has_error = True
    logging.debug('Add user! newuser info {}'.format(newuserinfo))

    while has_error:

        has_error = False
        if len(newuser) != userinfo_num:
            newuserinfo = input("User info has something wrong,Please input again:")
            newuser = newuserinfo.split(",")
            has_error = True
            logging.warning('Add user! newuser info has something wrong')
        else:
            name, age, tel, address = newuser

            if not age.isdigit():
                logging.warning('Add user! newuser age is wrong')
                print("\033[31m{}\033[0m".format("Input wrong age!".center(50, '*')))
                newuserinfo = input("User info has something wrong,Please input again:")
                newuser = newuserinfo.split(",")
                has_error = True


            elif not tel.isdigit():
                logging.warning('Add user! newuser tel is wrong')
                print("\033[31m{}\033[0m".format("Input wrong tel number!".center(50, '*')))
                newuserinfo = input("User info has something wrong,Please input again:")
                newuser = newuserinfo.split(",")
                has_error = True


            if not has_error:
                useridlist = user_id_mysql()
                maxid = int(max(useridlist)) + 1
                add_user_mysql(maxid,name,int(age),tel,address)
                print("\033[32m{}\033[0m".format("Add new user success".center(50, '*')))
                logging.debug('Add user! Add success, new user info {}'.format(newuserinfo))


'''
删除用户
'''
def del_users():
    deleteid = input("Please input your want to delete user ID: ")
    deleteexcel = PrettyTable(["ID", "NAME", "AGE", "TEL", "ADDRESS"])
    useridlist = user_id_mysql()
    uid = int(deleteid)


    if deleteid.isdigit():

        if uid in useridlist:
            user = find_user_mysql(uid)
            deleteexcel.add_row(user)
            print(deleteexcel)
            logging.debug('Del user! user info {}.'.format(user))
            answer = input("Do you sure want to delete this user:(Y/N)")

            if answer.upper() == 'Y':
                del_user_mysql(uid)
                print("\033[32m{}\033[0m".format("Delete user success".center(50, '*')))
                logging.debug('Del user! Delete user success.')
            elif answer.upper() == 'N':
                print("\033[34m{}\033[0m".format("OK! we will exit!".center(50, '*')))
                logging.debug('Del user! admin do not delete user.')
            else:
                print("\033[31m{}\033[0m".format("Invilad options!".center(50, '*')))
                logging.debug('Del user! Invilad options.')
        else:
            print("\033[31m{}\033[0m".format("Input wrong ID".center(50, '*')))
            logging.warning('Del user! Input wrong ID')
    else:
        print("\033[31m{}\033[0m".format("Sorry,not found user ID".center(50, '*')))
        logging.warning('Del user! not found user ID')

'''
更新用户信息
'''
def update_users():
    is_exists = False
    updateid = input("Please input your want to update user ID: ")
    updatexcel = PrettyTable(["ID", "NAME", "AGE", "TEL", "ADDRESS"])
    useridlist = user_id_mysql()
    updateuser = []

    if updateid.isdigit():
        if int(updateid) in useridlist:
            user = find_user_mysql(int(updateid))
            updatexcel.add_row(user)
            print(updatexcel)
            is_exists = True
            logging.debug('Update user! Update user info {}.'.format(user))
        else:
            print("\033[31m{}\033[0m".format("Sorry,not found user ID".center(50, '*')))
            logging.warning('Update user! not found user ID')

    if is_exists:
        newartt = input("Please input your want to update attributes:(name,age,tel or address):")
        if newartt not in ['name', 'age', 'tel', 'address']:
            print("\033[31m{}\033[0m".format("Invilad attributes!".center(50, '*')))
            logging.warning('Update user! Invilad attributes!')

        else:
            newarttinfo = input("Please input new {}: ".format(newartt))

            if newartt == 'age' or newartt == 'tel':
                if newarttinfo.isdigit():
                    update_user_mysql(newartt,newarttinfo,int(updateid))
                    logging.debug('Update user! Update user success. user info {}'.format(updateuser))

                else:
                    print("\033[31m{}{}\033[0m".center(50, '*').format("Input wrong ", newartt))
                    logging.warning('Update user! Input wrong {}'.format(newartt))
            else:
                update_user_mysql(newartt, newarttinfo, int(updateid))
                print("\033[32m{}\033[0m".format("Update user success".center(50, '*')))
                logging.debug('Update user! Update user success. user info {}'.format(updateuser))

'''
查找用户
'''
def find_users():
    findexcel = PrettyTable(["ID", "NAME", "AGE", "TEL", "ADDRESS"])
    findartt = input("Please input your want to find user info(ID,NAME,AGE,TEL OR ADDRESS):")
    find_flag = False

    userlist = list_user_mysql()
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

def export_users():
    fileexport = ReadConfig('config.ini', 'EXPORT', 'EXPORTFILE')
    userlist = list_user_mysql()
    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)

    keys = ['id', 'name', 'age', 'tel', 'address']

    for x in range(len(keys)):
        booksheet.write(0, x, keys[x])

    for i in range(len(userlist)):
        for j in range(len(userlist[i])):
            booksheet.write(i + 1, j, userlist[i][keys[j]])

    workbook.save(fileexport)
    print("\033[32m{}\033[0m".format("Export users to excel success".center(50, '*')))

'''
退出系统，保存用户信息
'''
def exit_users():
    print("\033[31m{}\033[0m".format("Log out!".center(50, '*')))
    exit()

'''
管理员操作
'''
def op_users():

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
                    "X or x  ---> Export users to excel file\n"
                    "E or e  ---> Exit system")
            op = input("Please input your action:")

            if op.upper() == 'L':
                list_users()
            elif op.upper() == 'A':
                  add_users()
            elif op.upper() == 'D':
                  del_users()
            elif op.upper() == 'U':
                  update_users()
            elif op.upper() == 'F':
                find_users()
            elif op.upper() == 'X':
                 export_users()
            elif op.upper() == 'E':
                 exit_users()
            else:
                print("\033[31m{}\033[0m".format("Invalid cmd".center(50, '*')))