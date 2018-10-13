import json
import time
import datetime
import math
import configparser
import os
import xlwt,xlrd
import jinja2
import prettytable
import output_log
import dbmysql
import output_file

config = configparser.ConfigParser()
config.read('conf.ini')

MAX_LOGIN_TIMES = config['CONF']['MAX_LOGIN_TIMES']
PAGE_LIST = int(config['CONF']['page_list'])

db,mysqldb = dbmysql.open_mysql()


def insert():
    has_error = 0

    insert_name = input('请输入增加用户的姓名: ').strip()
    insert_age = input('请输入增加用户的年龄: ').strip()
    insert_tel = input('请输入增加用户的电话: ').strip()
    insert_add = input('请输入增加用户的地址: ').strip()
    insert_create_time = int(time.time())
    insert_update_time = int(time.time())

    if len(insert_tel) < 7 or len(insert_name) < 1:
        has_error = 1
    if not insert_age.isdigit() or int(insert_age) < 1 or int(insert_age) > 200:
        has_error = 1
    if has_error:
        print('Illegal,输入非法↓')
        output_log.log_log('warn', '增加用户信息错误')
        return False
    print('\033[34m这是新增的信息，请核对:\033[0m')
    insert_dict = {'name': insert_name, 'age': insert_age, 'tel': insert_tel,'address': insert_add}
    print(insert_dict)
    change_flag = input('是否进行插入？(Y,y) 否则不更改 ')
    if change_flag == 'Y' or change_flag == 'y':

        try:
            insert_sql = ("insert into message(name, age, tel, address,create_time,update_time) values ('{}', '{}', '{}', '{}', '{}', '{}');"
                          .format(insert_name, insert_age, insert_tel, insert_add, insert_create_time, insert_update_time))
            dbmysql.execute_mysql(mysqldb = mysqldb,sql = insert_sql)
            dbmysql.commit_mysql(db = db)
            print(insert_sql)
            # insert_sql = '''insert into message(name, age, tel, address,create_time,update_time) values (%s, %s, %s, %s, %s, %s);'''
            # mysqldb.execute(insert_sql, (insert_name, insert_age, insert_tel, insert_add, insert_create_time, insert_update_time))
            print('用户信息插入成功')
            output_log.log_log('debug', '增加用户信息')
            output_log.log_log('debug', insert_dict)
        except:
            dbmysql.rollback_mysql(db)
            print('数据库报错，未插入这个用户信息')
            output_log.log_log('debug', '数据库报错，未插入这个用户信息')
    else:
        print('手动取消，未插入这个用户信息')
        output_log.log_log('debug', '手动取消，未插入这个用户信息')

def select():
    user_select = []
    select_flag = 0
    select_word = input('查询的字符串: ').strip()
    select_sql = ("select * from message where uid like '%{}%' or name like '%{}%' or tel like '%{}%'or address like '%{}%';"
                 .format(select_word, select_word, select_word, select_word))
    output_log.log_log('warn', select_sql)
    dbmysql.execute_mysql(mysqldb = mysqldb,sql = select_sql)
    for i in mysqldb.fetchall():
        user_select.append(i)
        select_flag = 1
    if select_flag:
        max_page = math.ceil(len(user_select) / PAGE_LIST)
        break_flag = 0
        while 1:
            if break_flag == 1:
                break
            page = input('想看哪一页 (最大页码 %d): ' % max_page)
            if page.isdigit() and 0 < int(page) <= max_page:
                page_num = int(page)
                head_mess = prettytable.PrettyTable(["uid", "name", "age", "tel", "address", "createTime", "create_time", "updateTime", "update_time"])
                head_mess.align["uid"] = "l"
                head_mess.padding_width = 1
                for user in user_select[(page_num - 1) * PAGE_LIST : page_num * PAGE_LIST]:
                    head_mess.add_row(user)
                print(head_mess)

            else:
                print('输入页码非法，请重新输入页码. eg:1 -- %d ' % max_page)
                continue
            print()
            show_quit = input('是否要继续查看信息 (输入 \'Q或q\' 则退出 将查询信息进行导出csv/html模式，否则继续): ').strip()
            if show_quit == 'Q' or show_quit == 'q':
                break_flag = 1

    else:
        print('无数据')

    print('''
        1、导出csv 文件
        2、导出html 文件
        N/n、不进行导出
    ''')

    choice = input('请选择导出csv或者html文件(N/n 不进行导出)：')
    # mysqldb.execute(select_sql)
    # output_mess = prettytable.from_db_cursor(mysqldb)
    # print(output_mess)
    if choice == "1":
        output_file.output_csv(user_select)

    elif choice == "2":
        output_file.output_html(user_select)

    elif choice == "N" or choice == "n":
        output_file.dont_output()

    else:
        output_file.illegal()

def update():
    has_error = 0
    Uselect_flag = 0

    update_uid = input('请输入更新用户的id: ').strip()
    if update_uid.isdigit():

        Uselect_sql = "select * from message where uid='{}' limit 1;".format(update_uid)
        dbmysql.execute_mysql(mysqldb = mysqldb,sql = Uselect_sql)
        for i in mysqldb.fetchall():
            print('这是要改的原数据→')
            print(i)
            Uselect_flag = 1
            break
        else:
            print('Sorry, 没有这个用户id')
            output_log.log_log('debug', update_uid)
            output_log.log_log('debug', '更新数据，没有这个id用户信息')

        if Uselect_flag:
            update_name = input('请输入更新用户的姓名: ').strip()
            update_age = input('请输入更新用户的年龄: ').strip()
            update_tel = input('请输入更新用户的电话: ').strip()
            update_add = input('请输入更新用户的地址: ').strip()
            update_update_time = int(time.time())
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
                update_sql = ("update message set name='{}', age='{}', tel='{}', address='{}', update_time='{}' where uid='{}';"
                              .format(update_name, update_age, update_tel, update_add, update_update_time, update_uid))
                update_message = {'name': update_name, 'age': update_age, 'tel': update_tel,'address': update_add}
                print(update_message)
                change_flag = input('这是是更改的信息，请核对 是否更改？(Y|y) 否则不更改: ')
                if change_flag == 'Y' or change_flag == 'y':
                    dbmysql.execute_mysql(mysqldb = mysqldb,sql = update_sql)
                    dbmysql.commit_mysql(db = db)
                    print('用户信息更新成功')
                    output_log.log_log('debug', '更新用户信息')
                    output_log.log_log('debug', update_sql)
                    output_log.log_log('debug', update_message)
                else:
                    print('未进行更新')
                    output_log.log_log('debug', '手动取消，未更改这个用户信息')
            else:
                print('请重新更新用户数据')
                output_log.log_log('warn', '修改用户输入信息错误')

    else:
        print('Sorry, id非法')
        output_log.log_log('warn', '更新输入id非法')

def delete():
    has_error = 0
    Dselect_flag = 0

    delete_uid = input('请输入删除用户的id: ').strip()
    if delete_uid.isdigit():

        Dselect_sql = "(select * from message where uid='{}' limit 1);".format(delete_uid)
        dbmysql.execute_mysql(mysqldb = mysqldb,sql = Dselect_sql)
        for i in mysqldb.fetchall():
            print('这是要删的原数据→')
            print(i)
            output_log.log_log('debug', i)
            output_log.log_log('debug', '准备删除这个id的信息')
            Dselect_flag = 1
            break
        else:
            print('Sorry, 没有这个用户id')

        if Dselect_flag:
            if not has_error:
                delete_sql = "delete from message where uid='{}';".format(delete_uid)
                delete_flag = input('这是是更改的信息，请核对 是否更改？(Y|y) 否则不更改: ')
                if delete_flag == 'Y' or delete_flag == 'y':
                    try:
                        dbmysql.execute_mysql(mysqldb = mysqldb,sql = delete_sql)
                        dbmysql.commit_mysql(db = db)
                        print('用户信息删除成功')
                        output_log.log_log('debug', '删除用户信息成功')
                    except:
                        dbmysql.rollback_mysql(db = db)
                        print('数据删除失败，已回滚')
                else:
                    print('未进行删除')
                    output_log.log_log('debug', '手动取消，未删除这个用户信息')
            else:
                print('请重新进行删除用户数据')
                output_log.log_log('warn', '删除用户输入id错误')

    else:
        print('Sorry, id非法')
        output_log.log_log('warn', '更新输入id非法')

def exit_system():
    print()
    print('用户信息保存成功，退出成功，bye-bye ~')
    break_flag = 1
    dbmysql.close_mysql(db,mysqldb)
    output_log.log_log('debug', '退出系统，关闭数据库连接')
    return break_flag

def other_action():
    print()
    print('你输入操作的动作非法')
    output_log.log_log('warn', '输入操作非法')

