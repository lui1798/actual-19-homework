# 用户信息管理系统
# 可以实现以下功能：
# 1、账户1天只能登陆失败3次，超过失败次数则锁定。
# 2、密码进行密文输入
# 3、对用户信息的增删改查操作，查看可以分页展示(改版的暂未实现)
# 4、对数据进行存储到数据库，方便以后读取
# 5、打印追加日志到 error.log 里

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# write by caozhi, 2018-09-15, version:5.0

from time import time
import pickle
import math
import logging
import requests
import json
import getpass
import configparser
import pymysql



config = configparser.ConfigParser()
config.read('conf.ini')

LOGFILE = config['LOG']['LOGFILE']
my_name = config['CONF']['my_name']
MAX_LOGIN_TIMES = config['CONF']['MAX_LOGIN_TIMES']
page_list = config['CONF']['page_list']
break_flag = 0
has_error = 0
payload = {'key1': 'value1', 'key2': 'value2'}


# 定义日志等级和输出信息
def log_log(level='debug',action='message'):
    logging.basicConfig(level=logging.DEBUG,
                format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                datefmt='%Y-%m-%d %I:%M:%S %p',
                filename=LOGFILE,
                filemode='a'
                )

    if level == 'debug':
        logging.debug(action)
    elif level == 'info':
        logging.info(action)
    elif level == 'warn':
        logging.warn(action)
    elif level == 'error':
        logging.error(action)
    else:
        logging.critical(action)


# 登陆函数
def login_yt():
    now_time = time()
    lasttime = float(config['CONF']['lasttime'])
    count = int(config['CONF']['count'])
    usermessage = {'count': count, 'lasttime': lasttime}
    usermessage['lasttime'] = now_time
    config.set("CONF", "lasttime", str(now_time))
    config.write(open('conf.ini', "w"))
    #with open('file', 'wb') as a:
    #    pickle.dump(usermessage, a)
    
    drop = now_time - lasttime
    # 判断是否大于1天
    if int(drop) > 60:
        usermessage['count'] = MAX_LOGIN_TIMES
    
    count = int(usermessage.get('count'))
    is_login = 0
    for i in range(count):
        TOKEN = getpass.getpass('\033[33m 请输入你的TOKEN(5775cbe26a3a3b153a3be6e68b9925e8db10557e): \033[0m').strip()
        headers = {'Authorization': 'token ' + TOKEN}
        #user_name = input('\033[33m 请输入你的姓名: \033[0m').strip()
        #password = getpass.getpass('\033[33m 请输入你的密码: \033[0m').strip()
        
        req = requests.get('https://api.github.com/user', headers=headers, params=payload)
        log_log('info', json.dumps(req.json()))
        log_log('info', req.url)
        res = req.json()

        #if user_name == usermessage['name'] and password == usermessage['passwd']:
        print("********* %s, %s ********" % (res.get("login",None),my_name))
        if res.get("login",None) == my_name:
            print('\033[32m login success ---> 登陆成功 \033[0m')
            is_login = 1
            break
        else:
            count -= 1
            usermessage['count'] = count
            config.set("CONF", "count", str(count))
            config.write(open('conf.ini', "w"))
            #with open('file', 'wb') as a:
            #    pickle.dump(usermessage, a)
            print('用户信息错误，登陆失败，还有 %d 次机会' % count)
            log_log('warn', '用户信息错误，登陆失败')
    
    else:
        print('\033[31m请在 60秒后(为调试方便，使用60s，可自定义调整)重试， 或者联系我...\033[0m')
        log_log('warn', '用户信息错误，登陆失败，已锁定')
    return(is_login)

def main():
    if is_login:
        log_log('debug','登陆成功')
        print('=' * 70)
        print('''
    \033[31m欢迎来到某某信息管理系统 \033[0m
    ''')
        print('=' * 70)
        server_ip = config['MYSQL']['server_ip']
        user = config['MYSQL']['user']
        passwd = config['MYSQL']['passwd']
        db = pymysql.connect(server_ip, user, passwd, "USERMESSAGE")
        mysqldb = db.cursor()
        print('连接数据库')
        log_log('debug','连接数据库了')
        while 1:
            print('''
     执行操作的序号:
     1、 插入一个用户信息.
     2、 查询当前用户信息.
     3、 更新某个用户信息.
     4、 删掉某个用户信息.
     5、 退出系统，并保存所有操作.
                ''')
            # 输入对用户信息的操作 按数据库逻辑实现,id 为主键
            action = input('\033[34m请输入需要执行操作的序号: \033[0m').strip()
    
            # 添加用户信息
            if action == '1':
                has_error = 0

                insert_name = input('请输入增加用户的姓名: ').strip()
                insert_age = input('请输入增加用户的年龄: ').strip()
                insert_tel = input('请输入增加用户的电话: ').strip()
                insert_add = input('请输入增加用户的地址: ').strip()
                insert_create_time = int(time())
                insert_update_time = int(time())

                if len(insert_tel) < 7 or len(insert_name) < 1:
                    has_error = 1
                if not insert_age.isdigit() or int(insert_age) < 1 or int(insert_age) > 200:
                    has_error = 1
                if has_error:
                    print('Illegal,输入非法↓')
                    log_log('warn', '增加用户信息错误')
                    continue
                print('\033[34m这是新增的信息，请核对:\033[0m')
                insert_dict = {'name': insert_name, 'age': insert_age, 'tel': insert_tel,'address': insert_add}
                print(insert_dict)
                change_flag = input('是否进行插入？(Y,y) 否则不更改 ')
                if change_flag == 'Y' or change_flag == 'y':
                    
                    try:
                        insert_sql = "insert into message(name, age, tel, address,create_time,update_time) values ('{}', '{}', '{}', '{}', '{}', '{}');".format(insert_name, insert_age, insert_tel, insert_add, insert_create_time, insert_update_time)
                        mysqldb.execute(insert_sql)
                        # insert_sql = '''insert into message(name, age, tel, address,create_time,update_time) values (%s, %s, %s, %s, %s, %s);'''
                        # mysqldb.execute(insert_sql, (insert_name, insert_age, insert_tel, insert_add, insert_create_time, insert_update_time))
                        db.commit()
                        print('用户信息插入成功')
                        log_log('debug', '增加用户信息')
                        log_log('debug', insert_dict)
                    except:
                        db.rollback()
                        print('数据库报错，未插入这个用户信息')
                        log_log('debug', '数据库报错，未插入这个用户信息')
                else:
                    print('手动取消，未插入这个用户信息')
                    log_log('debug', '手动取消，未插入这个用户信息')
                    # print(userinfo)
    
            # 查询某个用户信息
            elif action == '2':
                has_error = 0
                user_select = []
                select_sth = input('查询的字符串: ').strip()
                for user in userinfo:
                    if select_sth == '' or user.get('name').find(select_sth) != -1 or user.get('tel').find(select_sth) != -1 or user.get('address').find(select_sth) != -1:
                        user_select.append(user)  # 都写到内存里 会占用大量内存 待优化
                        print(user_select,'=====================')
                if len(user_select) == 0:
                    print('无数据')
                else:
                    # [i for i in userinfo if i.get('name') == select_name]
                    max_page = math.ceil(len(user_select) / page_list)
                    break_flag = 0
                    while 1:
                        if break_flag == 1:
                            break
                        page = input('想看哪一页 (最大页码 %d): ' % max_page)
                        TABLE_TPL = '{id:^7}|{name:^10}|{age:^5}|{tel:^13}|{address:^13}'
                        TABLE_SPLIT_LINE = 56
                        TABLE_TITLE = {"id": "id", "name": "name", "age": "age", "tel": "tel", "address": "address"}
                        TABLE_TPL.format(**TABLE_TITLE)
                        if page.isdigit() and 0 < int(page) <= max_page:
                            page_num = int(page)
                            print(TABLE_TPL.format(**TABLE_TITLE))
                            print('-' * TABLE_SPLIT_LINE)
                            for user in user_select[(page_num - 1) * page_list : page_num * page_list]:
                                print(TABLE_TPL.format(**user))
                            # for m in userinfo[page_list * (page_num - 1):page_list * page_num]:
                            #    print(m)
                        else:
                            print('输入页码非法，请重新输入页码. eg:1 -- %d ' % max_page)
                            continue
                        print()
                        show_quit = input('是否要继续查看信息 (输入 \'N或n\' 则退出，否则继续): ').strip()
                        if show_quit == 'N' or show_quit == 'n':
                            break_flag = 1
    
            # 更新某个用户信息
            elif action == '3':
                update_flag = 0
                has_error = 0
                update = input('请输入更新信息的id: ').strip()
                j = 0
                if update.isdigit():
                    update_id = int(update)
                    for m in userinfo:
                        if update_id == m.get('id'):
                            update_flag = 1
                            break
                        j += 1
                    else:
                        print('Sorry, 没有这个用户id')
                else:
                    print('Sorry, id非法')
                if update_flag:
                    update_name = input('请输入更新用户姓名: ').strip()
                    update_age = input('请输入更新用户年龄: ').strip()
                    update_tel = input('请输入更新用户电话: ').strip()
                    update_add = input('请输入更新用户地址: ').strip()
                    if len(update_name) < 1:
                        has_error = 1
                        print('输入姓名非法')
                    if not update_age.isdigit() or int(update_age) < 1 or int(update_age) > 200:
                        has_error = 1
                        print('输入年龄非法')
                    if len(update_tel) < 7:
                        has_error = 1
                        print('输入电话非法')
                    if len(update_add) < 1:
                        has_error = 1
                        print('输入地址非法')
                    if not has_error:
                        print({'id': update_id, 'name': update_name, 'age': update_age, 'tel': update_tel,'address': update_add})
                        change_flag = input('这是是更改的信息，请核对 是否更改？(Y|y) 否则不更改 ')
                        if change_flag == 'Y' or change_flag == 'y':
                            userinfo[j] = {'id': update_id, 'name': update_name, 'age': int(update_age), 'tel': update_tel,'address': update_add}
                            print('用户信息更新成功')
                            log_log('debug', '更新用户信息')
                            log_log('debug', userinfo[j])
                        else:
                            print('未进行更新')
                    else:
                        print('请重新更新用户数据')
                        log_log('warn', '修改用户信息错误')
            # 删除某个用户信息
            elif action == '4':
                has_error = 0
                delete = input('请输入要删除的用户id: ').strip()
                if not delete.isdigit() or len(delete) < 1:
                    has_error = 1
                    print('输入id非法')
                    log_log('warn', '删除的输入id非法')
                    continue
                delete_id = int(delete)
                n = 0
                delete_flag = 0
                for k in userinfo:
                    if delete_id == k.get('id'):
                        print(userinfo[n])
                        delete_flag = input('以下是删除的信息，请核对 是否删除？(Y|y) 否则不删除 ')
                        if delete_flag == 'Y' or delete_flag == 'y':
                            log_log('debug', '删除用户信息')
                            log_log('debug', userinfo[n])
                            userinfo.pop(n)
                            delete_flag = 1
                            print('用户信息删除成功')
                        else:
                            print('用户信息未进行删除')
                    n += 1
                if delete_flag == 0:
                    print('Sorry, 没有这个用户信息')
    
            # 退出整个系统
            elif action == '5':
                print()
                # 退出系统 自动将修改的内容写到磁盘中
                print('用户信息保存成功，退出成功，bye-bye ~')
                break_flag = 1
                db.close()
                break
            else:
                print()
                print('你输入操作的动作非法')
                log_log('warn', '输入操作非法')

if __name__ == '__main__':
    is_login = login_yt()
    main()
