#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-14 上午9:33
# @Author  : Uwei
# @File    : LoginAndInfo.py
password_list = {'admin': '1', 'wywmir': '1'}   #定义一个用户名密码字典
keyword_list = ['list', 'add', 'delete', 'update', 'find', 'exit']  #定义关键字的列表
user_info = [  # list
    [1, 'wyw1', '132xxx', 'beijing'],
    [2, 'wyw2', '132xxx', 'beijing'],
    [5, 'wyw3', '132xxx', 'shanghai'],
]
Tries = 3
while Tries > 0:
    loginname = input('请输入登录名:')
    password = input('请输入密码:')
    if loginname in password_list.keys() and password_list[loginname] == password:  #判断登录名在字典中，并且输入的登录名对应的密码和输入的密码匹配
        break
    elif Tries - 1 == 0:    #最后一次打印锁定
        print('用户被锁定')
        pass    #做点什么
        break
    else:
        print('用户名或密码错误，还有{}次机会'.format(Tries - 1))
        Tries -= 1

while True:
    op = input('请输入关键字(list,add,delete,update,find,exit): ')
    if op in keyword_list:
        if op == 'list':
            print(u'---------------------用户信息-------------------------\nid       name        tel             address ') #\n是打印回车
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
            else:
                uids = [x[0] for x in user_info]  # 列表推导式 第0个元素组成个新列表
                new_id = max(uids) + 1
                user_list.insert(0, new_id)
                user_info.append(user_list)
        elif op == 'delete':
            uid = input('输入要删除的行id:')
            for x in user_info:
                if x[0] == int(uid):
                    user_info.remove(x)
        elif op == 'update':
            selectuid = input(u'请输入： 行id :')
            for x in user_info:
                if x[0] == int(selectuid):
                    newbody = input(u'请输入新信息： name tel address 用空格分隔 :')
                    user_listnew = newbody.split(' ')
                    user_listnew.insert(0, selectuid)
                    user_info[int(selectuid) - 1] = user_listnew
#                    print(user_info)
        elif op == 'find':
            selectkey = input(u'请输入： 查找关键字 :')
            for i in user_info:  #解开下层列表
                if selectkey in i:
                    print(i)
        elif op == 'exit':
            break
    else:
        print('关键字输入错误')
