#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-8-15
# @Author  : mayulei

import time
import datetime
import json

password_list = ['admin','123456']
option_list=['0','1','2','3','4','5','6']
count = 3
user_keys = ['id', 'name','age','tel','addr']
TABLE_TPL = '{id:>10}|{name:>15}|{age:>5}|{tel:>15}|{addr:>20}'
TABLE_SPLIT_LINE = 64
TABLE_TITLE = {"id" : "id", "name" : "name", "age" : "age", "tel" : "tel" , "addr": "addr"}
user_values = []
lock_len =24*60*60


display_info='''
操作列表：
0、显示已有用户信息
1、增加用户信息
2、删除用户信息
3、修改用户信息
4、查询用户信息
5、保存用户信息
6、退出系统
'''

def list_fun(user_list):
    try:
        user_num = len(user_list)
        print('\033[34m用户信息数： {}\033[0m'.format(user_num))
        print(TABLE_TPL.format(**TABLE_TITLE))
        print('-' * TABLE_SPLIT_LINE)
        if user_num == 0:
            print('\033[31m暂无用户数据\033[0m')
        elif user_num <= 10:
            print(user_list)
        else:
            max_page = user_num // 10
            if user_num % 10:
                max_page += 1
            while True:
                text_page_num = input('共有1-{}页，输入显示页数：'.format(max_page))
                if text_page_num.isdigit() and int(text_page_num) <= max_page:
                    page_num = int(text_page_num)
                    print('-' * TABLE_SPLIT_LINE)
                    for user in user_list[(page_num - 1) * 10: page_num * 10]:
                        print(TABLE_TPL.format(**user))
                else:
                    print('\033[33m用户数据显示结束\033[0m')
                    break

    except:
        raise
        print('\033[31m显示用户信息程序发生异常\033[0m')

def load_info():
    try:
        fd = open('user.txt')
        user_info1 = fd.read()
        user_list = json.loads(user_info1)
        return user_list
    except:
        print('\033[31m保存用户数据异常\033[0m')
    finally:
        fd.close()

def is_lock(count):
    try:
        lock_flag = False
        while count > 0:

            login = input('请输入用户名:')
            password = input('请输入密码:')

            if count - 1 == 0 and lock_flag == False:
                lock_flag = True
                print('\033[31m输入用户名密码错误3次，用户被锁定\033[0m')
                lock_time = int(time.time())

            elif count - 1 == 0:
                wait_time = int(time.time()) - lock_time
                if int(time.time())-lock_time > lock_len:
                    count = 2
                    lock_flag = False
                    if login == password_list[0]  and password == password_list[1]:
                        break
                    else:
                        print('\033[31m用户名或密码错误，还有{}次机会\033[0m'.format(count))
                    continue

                else:
                    print('\033[31m用户被锁定,请{}秒后再输入\033[0m'.format(lock_len-wait_time))
            elif login == password_list[0]  and password == password_list[1]:
                break
            else:
                print('\033[31m用户名或密码错误，还有{}次机会\033[0m'.format(count - 1))
                count -= 1
    finally:
        print('\033[32m用户登陆成功\033[0m')

def add_user(user_list):
    input_info = input('请按照以下格式输入用户信息： name age tel address :')
    user_values = input_info.split(' ')
    if len(user_values) != 4:
        return
    user_values.insert(0, max([x['id'] for x in user_list]+[0])+1)
    user_info = dict(zip(user_keys, user_values))
    user_list.append(user_info)
    print("\033[32m用户已添加\033[0m")
    print(TABLE_TPL.format(**TABLE_TITLE))
    print(TABLE_TPL.format(**user_list[-1]))

    return

def update_user(user_list):
    try:
        user_id = input('请输入需要修改信息的用户ID:')
        for x in user_list:
            if str(x['id']) == user_id:
                while True:
                    user_info = input('请输入需要修改的内容（name/age/tel/addr）:')
                    if user_info == 'name':
                        user_name = input('请输入新用户名:')
                        x['name'] = user_name
                        print("\033[32m用户名修改成功\033[0m")
                        update_flag = input('是否继续修改（y/n）:')
                        if update_flag == 'y':
                            continue
                        else:
                            break
                    elif user_info == 'age':
                        user_tel = input('请输入新年龄:')
                        x['age'] = user_tel
                        print("\033[32m年龄修改成功\033[0m")
                        update_flag = input('是否继续修改（y/n）:')
                        if update_flag == 'y':
                            continue
                        else:
                            break
                    elif user_info == 'tel':
                        user_tel = input('请输入新手机号:')
                        x['tel'] = user_tel
                        print("\033[32m手机号修改成功\033[0m")
                        update_flag = input('是否继续修改（y/n）:')
                        if update_flag == 'y':
                            continue
                        else:
                            break
                    elif user_info == 'addr':
                        user_add = input('请输入新地址:')
                        x['addr'] = user_add
                        print("\033[32m地址修改成功\033[0m")
                        update_flag = input('是否继续修改（y/n）:')
                        if update_flag == 'y':
                            continue
                        else:
                            break
                    else:
                        print("\033[32m输入错误\033[0m")
                        update_flag = input('是否放弃修改（y/n）:')
                        if update_flag == 'y':
                            break
                break
        else:
            print("\033[31m无此ID用户\033[0m")
    except:
        print('\033[31m修改程序发生异常\033[0m')
    else:
        print("\033[32m修改完成\033[0m")
    return user_list

def delete_user(user_list):
    user_id = input('输入要删除的用户ID:')
    id_list = [str(x['id']) for x in user_list]
    if user_id in id_list:
        for x in user_list:
            if x['id'] == int(user_id):
                user_list.remove(x)
                print("\033[32m用户已删除\033[0m")
    else:
        print("\033[31m无此ID用户\033[0m")
    return user_list

def search_user(user_list):
    input_info = input('请输入，查找关键字 :')
    find_list = []
    for user_x in user_list:
        if input_info in user_x.values():
            find_list.append(user_x)
    if len(find_list) != 0:
        print(TABLE_TPL.format(**TABLE_TITLE))
        for user in find_list:
            print(TABLE_TPL.format(**user))
    else:
        print('\033[31m未有相关用户\033[0m')
    return user_list

def save_user(user_list):
    try:
        user_info = json.dumps(user_list)
        fd=open('user.txt','w')
        fd.write(user_info)
    except:
        print('\033[31m保存用户数据异常\033[0m')
    finally:
        fd.close()

is_lock(count)
user_list = load_info()

while True:
    print(display_info)
    option = input('请选择对应操作：')
    if option in option_list:
        if option == option_list[0]:
            list_fun(user_list)
        elif option == option_list[1]:
            add_user(user_list)
        elif option == option_list[2]:
            delete_user(user_list)
        elif option == option_list[3]:
            update_user(user_list)
        elif option == option_list[4]:
            search_user(user_list)
        elif option == option_list[5]:
            save_user(user_list)
        elif option == option_list[6]:
            save_user(user_list)
            break
    else:
        print('\033[32m请再次选择操作\033[0m')


