#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-14 上午9:33
# @Author  : Uwei
# @File    : LoginAndInfo.py
import os

# password_list = {'admin': '1', 'wywmir': '1'}  # 定义一个用户名密码字典
keyword_list = ['list', 'add', 'delete', 'update', 'find', 'exit']  # 定义关键字的列表
user_info = [  # list
    [1, 'wyw1', '132xxx', 'beijing'],
    [2, 'wyw2', '132xxx', 'shenyang'],
    [5, 'wyw3', '132xxx', 'shanghai'],
    [6, 'wyw5', '132xxx', 'shanghai'],
]
pwd=os.getcwd()
password_list={}
try:
    with open(pwd+'/'+'password_list', 'r') as f:
        for line in f:
            a=line.strip().split()
            password_list[a[0]]=a[1]

except Exception as e:
    print (e)
Tries = 3

while Tries > 0:
    loginname = input('请输入登录名:')
    password = input('请输入密码:')
    login_flag= 'off'

    if loginname in password_list.keys() and password_list[loginname] == password:  # 判断登录名在字典中，并且输入的登录名对应的密码和输入的密码匹配
        login_flag = 'on'
        break
    elif Tries - 1 == 0:  # 最后一次打印锁定
        print('\033[31m用户被锁定5分钟\033[0m')
        pass  # 做点什么
        break
    else:
        print('\033[31m用户名或密码错误，还有{}次机会\033[0m'.format(Tries - 1))
        Tries -= 1

while login_flag == 'on':
    op = input('请输入关键字(list,add,delete,update,find,exit): ')

    if op in keyword_list:
        if op == 'list':
            print(
                u'---------------------用户信息-------------------------\nid       name        tel             address ')  # \n是打印回车
            for i in user_info:
                for x in i:
                    print(x, '\t', '\t', end=' ')
                print()

        elif op == 'add':
            body = input(u'请输入： name tel address 用空格分隔 :')
            user_list = body.split(' ')  # 将输入的字符串，按空格分隔
            if len(user_info) == 0:  # 如果原有用户信息列表为空
                user_list.insert(0, 1)  # 列表第0个未知，插入数值1
                user_info.append(user_list)  # 将输入的信息加到id 1 后面
                print("\033[32m用户已添加\033[0m")
            else:
                uids = [x[0] for x in user_info]  # 列表推导式 第0个元素组成个新列表
                new_id = max(uids) + 1  #新的udi是最大的+1
                user_list.insert(0, new_id) #在列表第0个违章插入新id
                user_info.append(user_list)
                print("\033[32m用户已添加\033[0m")

        elif op == 'delete':
            uid = input('输入要删除的行id:')
            for x in user_info:
                if x[0] == int(uid):    #判断输入的id等于第几行的第0个
                    user_info.remove(x)
                    print("\033[32m用户已删除\033[0m")

        elif op == 'update':
            selectold = input(u'请输入关键字查找 :')
            print(u'---------------------用户信息-------------------------\nid       name        tel             address ')  # \n是打印回车
            for i in user_info:
                if selectold in i:
                    for x in i:
                        print(x, '\t', '\t', end=' ')
                        # print (user_info.index(i))
                    print()
            selectuid = input(u'请输入要修改的行id :')
            newbody = input(u'请输入新信息： name tel address 用空格分隔 :')
            newuser_list = selectuid.split(' ') + newbody.split(' ')    #输入的id转列表再合并
            for x in user_info:
                if x[0] == int(selectuid):
                    sid = user_info.index(x)    #找到输入id对应的列表索引
                    user_info[sid] = newuser_list
                    print("\033[32m用户已更新\033[0m")
        #    方法2
        #     id_list = [] 把id放到列表里
        #     for i in user_info:
        #         id_list.append(i[0])
        #     select_index = id_list.index(int(selectuid)) #找到输入的id对应的列表索引
        #     user_info[select_index] = newuser_list
        elif op == 'find':
            selectkey = input(u'请输入： 查找关键字 :')
            for i in user_info:  # 解开下层列表
                if selectkey in i:
                    print(i)

        elif op == 'exit':
            break
    else:
        print('关键字输入错误')