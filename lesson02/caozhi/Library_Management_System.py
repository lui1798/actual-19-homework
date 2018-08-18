#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author emmby,2018-08-15 version:2.3
# 图书馆信息管理系统

# 登陆函数，并判断是否失败超过3次，写入到文件
def login():
    global user_name, password, count
    with open('/home/caozhi/file', 'r') as f:
        count = int(f.read())
    if count == 0:
        print('Please contact super manager!')
        exit(1)
    user_name = input('\033[33m Please enter your user_name: \033[0m')
    password = input('\033[33m Please enter your password: \033[0m')


# 管理员用户和密码
usermessage = ('admin', 'playbook')
# 用户信息，id，姓名，年龄，电话，籍贯
userinfo = [
    [1, 'caozhi', 25, '0419', 'liaoyang'],
    [2, 'emmby', 25, '010', 'beijing'],
    [3, 'xiaozhi', 25, '0429', 'huludao'],
    [5, 'xuwei', 50, '029', 'xian'],
    [8, 'pushu', 45, '010', 'beijing'],
]

while 1:
    login()
    if user_name == usermessage[0] and password == usermessage[1]:
        print('\033[32m login success \033[0m')

        # 登陆欢迎信息
        print('=' * 80)
        print('''
\033[31mWelcome to come Liaoning Project Technology University library management system \033[0m
''')
        print('=' * 80)
        while 1:
            print('''
         Please enter an action:
         1、"insert": insert a record.
         2、"select": select someone message.
         3、"show": show all message.
         4、"update": update someone message.
         5、"delete": delete someone message.
         6、"quit": quit this system.
                ''')
            # 输入对用户信息的操作 按数据库逻辑实现,id 为主键
            action = input('\033[34mPlease enter your action: \033[0m')

            if action == 'insert':
                insert_id = userinfo[-1][0] + 1
                insert_name = input('Please enter add name: ')
                insert_age = int(input('Please enter add age: '))
                insert_tel = input('Please enter add tel: ')
                insert_add = input('Please enter add address: ')
                userinfo.append([insert_id, insert_name, insert_age, insert_tel, insert_add])
                print()
                print(userinfo[-1])

            elif action == 'select':
                select_name = input('Please enter select name: ')
                select_flag = 0
                for i in userinfo:
                    if select_name == i[1]:
                        print(i)
                        select_flag = 1
                if select_flag == 0:
                    print('Sorry, record empty')

            elif action == 'update':
                update_id = int(input('Please enter update student id: '))
                update_flag = 0
                j = 0
                for m in userinfo:
                    if update_id == m[0]:
                        update_name = input('Please enter update name: ')
                        update_age = int(input('Please enter update age: '))
                        update_tel = input('Please enter update tel: ')
                        update_add = input('Please enter update address: ')
                        update_flag = 0
                        userinfo[j] = [update_id, update_name, update_age, update_tel, update_add]
                        print(userinfo[j])
                        update_flag = 1
                    j += 1
                if update_flag == 0:
                    print('Sorry, record empty')

            elif action == 'delete':
                delete_id = int(input('Please enter delete student id: '))
                n = 0
                delete_flag = 0
                for k in userinfo:
                    if delete_id == k[0]:
                        userinfo.pop(n)
                        delete_flag = 1
                    n += 1
                if delete_flag == 0:
                    print('Sorry, record empty')

            # 显示用户信息分页展示，默认每页显示3条
            elif action == 'show':
                if len(userinfo) % 3 == 0:
                    max_page = (len(userinfo) // 3)
                else:
                    max_page = (len(userinfo) // 3 + 1)
                while 1:
                    page = int(input('which page (0 for all): '))
                    if 0 < page <= max_page:
                        for m in userinfo[3 * (page - 1):3 * page]:
                            print(m)
                    elif page == 0:
                        for a in userinfo:
                            print(a)
                    else:
                        print('out of data,please enter correct page. eg:1 -- %d ' % max_page)
                    print()
                    show_quit = input('Weather continue show (\'N\' is quit): ')
                    if show_quit == 'N':
                        break

            elif action == 'quit':
                print()
                print('Exit success')
                exit(0)

            else:
                print()
                print('Your action is illegal')

    else:
        count -= 1
        with open('/home/caozhi/file', 'w') as f:
            f.write(str(count))
        print('login error, you have %d left choice' % count)
