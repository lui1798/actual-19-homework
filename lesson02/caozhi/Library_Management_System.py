#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author emmby,2018-08-15
# 图书管理系统

def login():
    global name, lpw
    if count == 0:
        print('please try tomorrow!')
        exit(1)
    name = input('Please enter your username: ')
    lpw = input('Please enter your password: ')

print('''
\033[31m Welcome to come Liaoning Project Technology University library management system \033[0m
''', end='')

usermessage = ('admin', 'playbook')
userinfo = [
    [1, 'caozhi', 25, '0419', 'liaoyang'],
    [2, 'emmby', 25, '010', 'beijing'],
    [3, 'xiaozhi', 25, '0429', 'huludao'],
    [5, 'xuwei', 50, '029', 'xian'],
    [8, 'pushu', 45, '010', 'beijing'],
]
count = 3
while 1:
    login()
    if name == usermessage[0] and lpw == usermessage[1]:
        print('\n\t\tlogin success')
        print('''
        Please an action
        "insert": insert a record.
        "select": select someone message.
        "update": update someone message.
        "delete": delete someone message.
        ''')
        action = input('\tenter your action: ')
        if action == 'insert':
            insert_id = userinfo[-1][0] + 1
            insert_name = input('add name: ')
            insert_age = int(input('add age: '))
            insert_tel = input('add tel: ')
            insert_add = input('add address: ')
            userinfo.append([insert_id, insert_name, insert_age, insert_tel, insert_add])
        elif action == 'select':
            select_name = input('enter select name: ')
            select_result = 0
            for i in userinfo:
                if select_name == i[1]:
                    print(i)
                    select_result = 1
            if select_result == 0:
                print('empty')
        elif action == 'update':
            pass
        elif action == 'delete':
            delete_id = int(input('enter delete id: '))
            k = 0
            delete_result = 0
            for j in userinfo:
                if delete_id == j[0]:
                    userinfo.pop(k)
                    delete_result = 1
                k += 1
            if delete_result == 0:
                print('empyt')
        elif action == 'exit':
            print('exit success')
            exit(0)
        else:
            print('your action is illegal')
    else:
        count -= 1
        print('login error,you have %d left choice' % count)
