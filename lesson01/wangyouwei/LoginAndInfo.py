#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-14 上午9:33
# @Author  : Uwei
# @File    : LoginAndInfo.py
password_list = {'admin': 'weiwei', 'wywmir': 'weiwei2009'}
keyword_list = ['list','add','delete','update','find','exit']
user_info = [  # list
    (1, 'test1', '132xxxx', 'beijing'),  # tuple
    (2, 'test2', '139xxxx', 'shanghai'),
    (3, 'test3', '135xxxx', 'zhengzhou'),
]
Tries = 3
while Tries > 0:
    loginname = input('请输入登录名:')
    password = input('请输入密码:')
    if loginname in password_list.keys() and password_list[loginname] == password:
        break

    elif Tries - 1 == 0:
        print('用户被锁定')
        pass
        break
    else:
        print('用户名或密码错误，还有{}次机会'.format(Tries - 1))
        Tries -= 1

while True:
    op = input('请输入关键字(list,add,delete,update,find,exit): ')
    if op in keyword_list:
        if op == 'list':
            print(u'---------------------------------------------------\nid       name        tel             adress ')
            for i in user_info:
                for x in i:
                    print(x, '\t', '\t', end=' ')
                print()
        if op == 'exit':
            break
    else:
        print('关键字输入错误')
