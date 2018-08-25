#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-8-15
# @Author  : mayulei
'''
用户管理系统：
1、登录认证；
2、增删改查；
3、格式化输出。

系统中存储用户信息如下：
id        name            tel             addr
1 	 	 mayulei 	 	  132xxx 	 	 shandong
2 	 	 wangqianong 	  132xxx         henan
...
'''
import time
import datetime
import json

fd=open('user.txt')
user_info1 = fd.read()
user_list = json.loads(user_info1)

password_list = ['admin','123456'] # 用户名密码

# user_list = [
#     {'id': 1, 'name': 'mayulei','age':'29' ,'tel': '188xxx','addr': 'shandong'},
#     {'id': 2, 'name': 'pangya', 'age': '28', 'tel': '187xxx', 'addr': 'henan'},
#     {'id': 3, 'name': 'wangqianlong1', 'age': '29', 'tel': '186xxx', 'addr': 'henan'},
#     {'id': 4, 'name': 'wangqianlong2', 'age': '29', 'tel': '186xxx', 'addr': 'henan'},
#     {'id': 5, 'name': 'wangqianlong', 'age': '29', 'tel': '186xxx', 'addr': 'henan'},
#     {'id': 6, 'name': 'wangqianlong6', 'age': '29', 'tel': '186xxx', 'addr': 'henan'},
#     {'id': 7, 'name': 'wangqianlong', 'age': '29', 'tel': '186xxx', 'addr': 'henan'},
#     {'id': 8, 'name': 'wangqianlong3', 'age': '29', 'tel': '186xxx', 'addr': 'henan'},
#     {'id': 9, 'name': 'wangqianlong', 'age': '29', 'tel': '186xxx', 'addr': 'henan'},
#     {'id': 10, 'name': 'wangqianlong4', 'age': '29', 'tel': '186xxx', 'addr': 'henan'},
#     {'id': 11, 'name': 'wangqianlong', 'age': '29', 'tel': '186xxx', 'addr': 'henan'},
#     {'id': 12, 'name': 'wangqianlong5', 'age': '29', 'tel': '186xxx', 'addr': 'henan'},
#     {'id': 13, 'name': 'wangqianlong7', 'age': '29', 'tel': '186xxx', 'addr': 'henan'},
#     {'id': 14, 'name': 'wangqianlong', 'age': '29', 'tel': '186xxx', 'addr': 'henan'},
#     {'id': 15, 'name': 'haoshan', 'age': '27', 'tel': '185xxx', 'addr': 'hebei'}
# ]
option_list=['0','1','2','3','4','5']
count = 3 #错误登录次数
user_keys = ['id', 'name','age','tel','addr']
user_values = []
lock_len =24*60*60
display_info='''
操作列表：
0、显示已有用户信息
1、增加用户信息
2、删除用户信息
3、修改用户信息
4、查询用户信息
5、退出系统
'''
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


print('\033[33m欢迎用户' + password_list[0] + '登录系统\033[0m')

while True:
    print(display_info)
    option = input('请选择对应操作：')
    if option in option_list:
        if option == option_list[0]:
            try:
                user_num = len(user_list)
                print('\033[34m用户信息数： {}\033[0m'.format(user_num))
                print('\033[34m{:<15}{:<15}{:<15}{:<15}{:<15}\033[0m'.format('ID', 'name', 'age', 'tel', 'addr'))
                user_pg = user_num // 10 + 1
                for i in range(user_pg):
                    for x in user_list[i * 10:i * 10 + 10]:
                        for y in x:
                            print('\033[33m{:<14}\033[0m'.format(x[y]), end=' ')
                        print()
                    if user_pg == 1:
                        break
                    input_info = input('是否继续显示用户信息,回车键继续显示，任意键结束显示:')
                    if input_info == '':
                        continue
                    else:
                        print('\033[34m显示用户信息中止\033[0m')
                        break
                # if user_num <=10 :
                #     for x in user_list:
                #         for y in x:
                #             print('\033[33m{:<14}\033[0m'.format(x[y]), end=' ')
                #         print()
                # else:


            except:
                print('\033[31m显示用户信息程序发生异常\033[0m')
        elif option == option_list[1]:
            input_info = input('请按照以下格式输入用户信息： name age tel address :')
            user_values = input_info.split(' ')  # 将输入的字符串，按空格分隔
            if len(user_values) != 4 :
                continue
            if len(user_list) == 0:  # 如果原有用户信息列表为空
                user_values.insert(0, 1)  # 列表第0个未知，插入数值1
                user_info = dict(zip(user_keys,user_values))
                user_list.append(user_info)  # 将输入的信息加到id 1 后面
                print("\033[32m用户已添加\033[0m")
            else:
                id_list = [x['id'] for x in user_list]  # 列表推导式 第0个元素组成个新列表
                new_id = max(id_list) + 1  #新的id是最大的+1
                user_values.insert(0, new_id) #在列表第0个违章插入新id
                user_info = dict(zip(user_keys, user_values))
                user_list.append(user_info)
                print("\033[32m用户已添加\033[0m")
                print('\033[34m{:<15}{:<15}{:<15}{:<15}{:<15}\033[0m'.format('ID', 'name', 'age', 'tel', 'addr'))
                for y in user_list[-1] :
                    print('\033[33m{:<14}\033[0m'.format(user_list[-1][y] ),end=' ')
        elif option == option_list[2]:
            user_id = input('输入要删除的用户ID:')
            id_list = [str(x['id']) for x in user_list]
            if user_id in id_list:
                for x in user_list:
                    if x['id'] == int(user_id):
                        user_list.remove(x)
                        print("\033[32m用户已删除\033[0m")
            else:
                print("\033[31m无此ID用户\033[0m")
        elif option == option_list[3]:
            user_id = input('请输入需要修改信息的用户ID:')
            id_list = [str(x['id']) for x in user_list]  # 列表推导式 第0个元素组成个新列表
            try:
                for x in user_list:
                    if x['id'] == int(user_id):
                        while True :
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
                            else :
                                print("\033[32m输入错误\033[0m")
                                update_flag = input('是否放弃修改（y/n）:')
                                if update_flag == 'y':
                                    break
                        break
            except:
                print('\033[31m修改程序发生异常\033[0m')
            else:
                print("\033[32m修改完成\033[0m")

        elif option == option_list[4]:
            input_info = input('请输入，查找关键字 :')
            find_list = []
            for user_x in user_list:
                if input_info in user_x.values():
                    find_list.append(user_x)
            if len(find_list)!= 0:
                print('\033[34m{:<15}{:<15}{:<15}{:<15}{:<15}\033[0m'.format('ID', 'name', 'age', 'tel', 'addr'))
                for x in find_list:
                    for y in x:
                        print('\033[33m{:<14}\033[0m'.format(x[y]), end=' ')
                    print()
            else:
                print('\033[31m未有相关用户\033[0m')
        elif option == option_list[5]:
            break
    else:
        print('\033[32m请再次选择操作\033[0m')

user_info = json.dumps(user_list)
fd=open('user.txt','w')
fd.write(user_info)
fd.close()

