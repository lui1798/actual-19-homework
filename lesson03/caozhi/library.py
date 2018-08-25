from time import time
import pickle

with open('file', 'rb') as f:
    usermessage = pickle.load(f)

with open('message', 'rb') as a:
    userinfo = pickle.load(a)
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

    # 判断可登录的剩余次数 是否=0
    count = usermessage.get('count')
    if count <= 0:
        now_time = time()
        lasttime = usermessage.get('lasttime')
        usermessage['lasttime'] = now_time
        with open('file', 'wb') as a:
            pickle.dump(usermessage,a)

        # 判断是否超过1天，如果少于1天则不允许登陆
        drop = now_time - lasttime
        if int(drop) > 30:
            usermessage['count'] = 3
            usermessage['lasttime'] = now_time
            with open('file','wb') as f:
                pickle.dump(usermessage,f)
            continue
        else:
            print('\033[31mPlease retry 30秒(为调试方便，使用30s，可自定义调整) later, or contact super manager!\033[0m')
            break_flag = 1
            break

    # 输入登陆信息
    user_name = input('\033[33m Please enter your user_name: \033[0m')
    password = input('\033[33m Please enter your password: \033[0m')

    if user_name == usermessage['name'] and password == usermessage['passwd']:
        print('\033[32m login success \033[0m')

        # 登陆欢迎信息
        print('=' * 80)
        print('''
\033[31mWelcome to come Liaoning Project Technology University library management system \033[0m
''')
        print('=' * 80)

        while 1:
            if break_flag:
                break
            print('''
 Please enter an action:
 1、 insert a record.
 2、 select someone message.
 3、 show all message.
 4、 update someone message.
 5、 delete someone message.
 6、 quit this system.
            ''')

            # 输入对用户信息的操作 按数据库逻辑实现,id 为主键
            action = input('\033[34mPlease enter your action: \033[0m')

            # 添加用户信息
            if action == '1':
                insert_id = int(userinfo[-1]['id']) + 1
                insert_name = input('Please enter add name: ')
                insert_age = int(input('Please enter add age: '))
                insert_tel = input('Please enter add tel: ')
                insert_add = input('Please enter add address: ')
                insert_dict = {'id': insert_id, 'name': insert_name, 'age': insert_age, 'tel': insert_tel, 'address': insert_add}
                userinfo.append(insert_dict)
                print('This is insert message:')
                print(userinfo[-1])

            # 查询某个用户信息
            elif action == '2':
                select_name = input('Please enter select name: ')
                select_flag = 0
                # [i for i in userinfo if i.get('name') == select_name]
                for i in userinfo:
                    if i.get('name', None) == select_name:
                        select_flag = 1
                        print(i)
                if select_flag == 0:
                    print('Sorry, record empty')

            # 显示所有用户信息，并分页展示，默认每页显示3条
            elif action == '3':
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

            # 更新某个用户信息
            elif action == '4':
                update_id = int(input('Please enter update student id: '))
                update_flag = 0
                j = 0
                for m in userinfo:
                    if update_id == m.get('id'):
                        update_name = input('Please enter update name: ')
                        update_age = int(input('Please enter update age: '))
                        update_tel = input('Please enter update tel: ')
                        update_add = input('Please enter update address: ')
                        userinfo[j] = {'id': update_id, 'name': update_name, 'age': update_age, 'tel': update_tel, 'address': update_add}
                        print(userinfo[j])
                        update_flag = 1
                    j += 1
                if update_flag == 0:
                    print('Sorry, record empty')

            # 删除某个用户信息
            elif action == '5':
                delete_id = int(input('Please enter delete student id: '))
                n = 0
                delete_flag = 0
                for k in userinfo:
                    if delete_id == k.get('id'):
                        userinfo.pop(n)
                        delete_flag = 1
                    n += 1
                if delete_flag == 0:
                    print('Sorry, record empty')

            # 退出整个系统
            elif action == '6':
                print()
                print('Exit success')
                break
                break_flag = 1
            else:
                print()
                print('Your action is illegal')

    else:
        count -= 1
        with open('/home/caozhi/file', 'w') as f:
            f.write(str(count))
        usermessage['count'] = count
        print('login error, you have %d left choice' % count)

# 将修改的内容写到磁盘中
with open('message','wb') as m:
    pickle.dump(userinfo,m)
