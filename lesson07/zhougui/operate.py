#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @File  : operate.py
# @Author: ZhouGui
# @Date  : 2018/9/9
# @Description : 用户增删改查操作
import math
import json
import logging
from utils import db
from utils import config
from utils.fmt import PrintTable
from utils.export import exportHtml
from utils.export import exportExcel

USER_INFO_NUM = 4

LOGFILE = config.ReadConfigFile('conf.ini', 'LOG', key='LOGFILE')
logger = logging.getLogger()
fh = logging.FileHandler(LOGFILE, encoding='utf-8')
fm = logging.Formatter('[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s')
fh.setFormatter(fm)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)


def add_user():
    text = input("请依次输入用户名，年龄，电话号码，地址, 信息使用空格分割:")
    user_list = text.split()
    if len(user_list) != USER_INFO_NUM:
        print("\033[1;31m 输入的用户信息有误\033[0m")
        logging.warning('用户信息输入有误')
    else:
        name = user_list[0]
        age = user_list[1]
        tel = user_list[2]
        address = user_list[3]
        has_Error = False
        if not age.isdigit():
            print("\033[1;31m 年龄输入有误\033[0m")
            logging.warning('年龄输入有误')
            has_Error = True
        if not tel.isdigit():
            print("\033[1;31m 电话号码输入有误\033[0m")
            logging.warning('电话号码输入有误')
            has_Error = True
        if not has_Error:
            db.add_user(
                "insert into user (username,age,tel,address) values('%s','%s','%s','%s')" % (name, age, tel, address))
            print("\033[32m用户{}添加成功\033[0m".format(name))
            logging.debug('用户{}添加成功,age:{},tel:{},address:{}'.format(name, age, tel, address))


def del_user():
    text = input("请输入删除用户的ID：")
    if text.isdigit():
        db.del_user("delete from user where id='%s'" % (text))
    else:
        print("\033[1;31m 输入参数有误\033[0m")


def change_user():
    text = input("请输入修改用户ID：")
    if text.isdigit():
        mod = input("Please choice your mod [username|age|tel|address]:")
        message = input("Please input your message:")
        db.update_user("update user set %s='%s' where id = '%s'" % (mod, message, text))
    else:
        print("\033[1;31m 输入参数有误\033[0m")


def query_user():
    users_find = []
    text = input("请输入ID查询:")
    if text.isdigit():
        user = db.select_user("select * from user where id = '%s'" % (text))
        if user:
            users_find.append(user)
        users_find_count = len(users_find)
        if users_find_count == 0:
            print("\033[1;31m 无数据\033[0m")
        else:
            print(users_find)
    else:
        print("\033[1;31m 输入参数有误\033[0m")


def list_user():
    fields = ['id', 'username', 'age', 'tel', 'address']
    sql = 'SELECT {} from user;'.format(','.join(fields))
    msg = db.select_user(sql)
    dataMsg = [dict(zip(fields, x)) for x in msg]
    users, _ = PrintTable(dataMsg)
    print(users)
    return '', True


def operate():
    while True:
        op = input("Please input your option [add|del|update|list|find|excel|html|exit]:")
        if op == "add":
            users = add_user()
        elif op == "del":
            del_user()
        elif op == "update":
            change_user()
        elif op == "list":
            list_user()
        elif op == "find":
            query_user()
        elif op == "excel":
            exportExcel('user.xls')
        elif op == "html":
            exportHtml()
        elif op == "exit":
            break
        else:
            print("\033[1;31m 输入参数有误\033[0m")
