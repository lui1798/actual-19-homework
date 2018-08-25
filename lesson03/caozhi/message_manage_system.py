#!/usr/bin/env python
# -*- coding: utf-8 -*-
# write by caozhi, 2018-08-23, version:3.2
# 用户信息管理系统


from time import time
import pickle

try:
    with open('file', 'rb') as f:
        usermessage = pickle.load(f)
except FileNotFoundError as eee:
    print(eee,'管理员用户文件异常')
    exit(1)

try:
    with open('message', 'rb') as a:
        userinfo = pickle.load(a)
except FileNotFoundError as fff:
    print(fff,'用户信息文件异常')
    exit(1)

# usermessage = {'name': 'admin', 'passwd': 'playbook', 'count': 3, 'lasttime': 1535080972.4686918}

# userinfo = [
# {'id': 1, 'name': 'name1', 'age': 20, 'tel': '132xxx', 'address': 'beijing'},
# {'id': 2, 'name': 'name2', 'age': 20, 'tel': '132xxx', 'address': 'beijing'},
# {'id': 3, 'name': 'name3', 'age': 20, 'tel': '132xxx', 'address': 'beijing'},
# {'id': 5, 'name': 'name4', 'age': 20, 'tel': '132xxx', 'address': 'beijing'},
# {'id': 8, 'name': 'name5', 'age': 20, 'tel': '132xxx', 'address': 'beijing'},
# {'id': 9, 'name': 'name6', 'age': 20, 'tel': '132xxx', 'address': 'beijing'}
# ]

break_flag = 0

while 1:
    if break_flag:
        break

    # 没有机会时，强制同步 最后登陆失败时时间戳
    now_time = time()
    usermessage['lasttime'] = now_time
    with open('file', 'wb') as a:
        pickle.dump(usermessage,a)
    # 判断可登录的剩余次数 是否=0
    count = usermessage.get('count')
    if count <= 0:
        lasttime = usermessage.get('lasttime')

        # 判断是否超过1天，如果少于1天则不允许登陆
        drop = now_time - lasttime
        if int(drop) > 60:
            usermessage['count'] = 3
            continue
        else:
            print('没有机会了~~~')
            print('\033[31m请在 60秒后(为调试方便，使用60s，可自定义调整)重试， 或者联系我...\033[0m')
            break_flag = 1
            break

    # 输入登陆信息
    user_name = input('\033[33m 请输入你的姓名: \033[0m').strip()
    password = input('\033[33m 请输入你的密码: \033[0m').strip()

    if user_name == usermessage['name'] and password == usermessage['passwd']:
        print('\033[32m login success ---> 登陆成功 \033[0m')

        # 登陆欢迎信息
        print('=' * 80)
        print('''
\033[31m欢迎来到某某信息管理系统 \033[0m
''')
        print('=' * 80)

        while 1:
            if break_flag:
                break
            print('''
 执行操作的序号:
 1、 插入一个用户信息.
 2、 查询当前某个用户信息.
 3、 展示所有用户信息.
 4、 更新某个用户信息.
 5、 删掉某个用户信息.
 6、 退出系统，并保存所有操作.
            ''')

            # 输入对用户信息的操作 按数据库逻辑实现,id 为主键
            action = input('\033[34m请输入需要执行操作的序号: \033[0m').strip()

            # 添加用户信息
            if action == '1':
                insert_id = int(userinfo[-1]['id']) + 1
                insert_name = input('请输入增加的姓名: ').strip()
                if len(insert_name) < 1:
                    print('Illegal,输入非法↓')
                    continue
                try:
                    insert_age = int(input('请输入年龄: ').strip())
                except:
                    print('输入类型错误')
                    continue
                else:
                    if insert_age < 1 or insert_age > 200:
                        print('Illegal,输入非法↓')
                        continue
                insert_tel = input('Please enter add tel: ').strip()
                if len(insert_tel) < 7:
                    print('Illegal,输入非法↓')
                    continue
                insert_add = input('Please enter add address: ').strip()
                if len(insert_add) < 1:
                    print('Illegal,输入非法↓')
                    continue
                insert_dict = {'id': insert_id, 'name': insert_name, 'age': insert_age, 'tel': insert_tel, 'address': insert_add}
                userinfo.append(insert_dict)
                print('这是新增的信息，请核对:')
                print(userinfo[-1])

            # 查询某个用户信息
            elif action == '2':
                select_name = input('请输入用户姓名: ').strip()
                if len(select_name) < 1:
                    print('Illegal,输入非法↓')
                    continue
                select_flag = 0
                # [i for i in userinfo if i.get('name') == select_name]
                for i in userinfo:
                    if i.get('name', None) == select_name:
                        select_flag = 1
                        print(i)
                if select_flag == 0:
                    print('Sorry, 没有这个用户信息')

            # 显示所有用户信息，并分页展示，默认每页显示3条
            elif action == '3':
                if len(userinfo) % 3 == 0:
                    max_page = (len(userinfo) // 3)
                else:
                    max_page = (len(userinfo) // 3 + 1)
                while 1:

                    try:
                        page = int(input('请输入查看的页码 (0 是全部): ').strip())
                    except:
                        print('输入类型错误')
                    else:
                        if 0 < page <= max_page:
                            for m in userinfo[3 * (page - 1):3 * page]:
                                print(m)
                        elif page == 0:
                            for a in userinfo:
                                print(a)
                        else:
                            print('超过了正常页数的范围，请重新输入页码. eg:1 -- %d ' % max_page)
                            continue
                        print()
                        show_quit = input('是否要继续查看信息 (输入 \'N或n\' 则退出，否则继续): ').strip()
                        if show_quit == 'N' or show_quit == 'n':
                            break

            # 更新某个用户信息
            elif action == '4':
                try:
                    update_id = int(input('请输入更新信息的id: ').strip())
                except:
                    print('输入类型错误')
                    continue
                update_flag = 0
                j = 0
                for m in userinfo:
                    update_flag = 1
                    if update_id == m.get('id'):
                        update_name = input('请输入更新用户姓名: ').strip()
                        if len(update_name) < 1:
                            print('Illegal,输入非法↓')
                            continue
                        try:
                            update_age = int(input('请输入更新用户年龄: ').strip())
                        except:
                            print('Illegal,输入非法↓')
                            break
                        else:
                            if update_age < 1 or update_age > 200:
                                print('Illegal,输入年龄非法↓')
                                continue
                        update_tel = input('请输入更新用户电话: ').strip()
                        if len(update_tel) < 1:
                            print('Illegal,输入非法↓')
                            continue
                        update_add = input('请输入更新用户地址: ').strip()
                        if len(update_add) < 1:
                            print('Illegal,输入非法↓')
                            continue
                        userinfo[j] = {'id': update_id, 'name': update_name, 'age': update_age, 'tel': update_tel, 'address': update_add}
                        print(userinfo[j])
                    j += 1
                if update_flag == 0:
                    print('Sorry, 没有这个用户id')

            # 删除某个用户信息
            elif action == '5':
                try:
                    delete_id = int(input('请输入要删除的用户id: ').strip())
                except:
                    print('Illegal,输入非法↓')
                    continue
                n = 0
                delete_flag = 0
                for k in userinfo:
                    if delete_id == k.get('id'):
                        userinfo.pop(n)
                        delete_flag = 1
                        print('用户信息删除成功')
                    n += 1
                if delete_flag == 0:
                    print('Sorry, 没有这个用户信息')

            # 退出整个系统
            elif action == '6':
                print()
                print('退出成功，bye-bye ~')
                break_flag = 1
                break
            else:
                print()
                print('你输入操作的动作非法')

    else:
        count -= 1
        with open('/home/caozhi/file', 'w') as f:
            f.write(str(count))
        usermessage['count'] = count
        print('用户信息错误，登陆失败，还有 %d 次机会' % count)

# 退出系统 自动将修改的内容写到磁盘中
with open('message','wb') as m:
    pickle.dump(userinfo,m)
