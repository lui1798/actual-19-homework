#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : taurusslq
# @Time    : 2018/9/12 下午11:06
# @File    : modulemysql.py
# @Software: PyCharm

import pymysql
from modulefile import ReadConfig

mysqlhost = ReadConfig('config.ini', 'MYSQL', 'HOST')
mysqluser = ReadConfig('config.ini', 'MYSQL', 'USER')
mysqlpass = ReadConfig('config.ini', 'MYSQL', 'PASSWORD')
mysqldata = ReadConfig('config.ini', 'MYSQL', 'DATABASE')
mysqlport = ReadConfig('config.ini', 'MYSQL', 'PORT')


conn = pymysql.connect(host=mysqlhost,user=mysqluser,password=mysqlpass,database=mysqldata,port=int(mysqlport))


def list_user_mysql():
    userlist = []
    sql = 'select * from usertable;'
    cursor = conn.cursor()
    cursor.execute(sql)
    for i in cursor.fetchall():
        userdict = {}
        userdict['id'] = i[0]
        userdict['name'] = i[1]
        userdict['age'] = i[2]
        userdict['tel'] = i[3]
        userdict['address'] = i[4]
        userlist.append(userdict)

    return userlist

def user_id_mysql():
    userid = []
    sql = '''select id from usertable'''
    cursor = conn.cursor()
    cursor.execute(sql)
    for i in cursor.fetchall():
        userid.append(int(i[0]))

    return userid


def add_user_mysql(userid,username,userage,usertel,useraddress):
    sql = "insert into usertable(id,name,age,tel,address) values('%d','%s','%d','%s','%s');" % (userid,username,userage,usertel,useraddress)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

def del_user_mysql(userid):
    sql = """delete from usertable where id = '%d';""" %(userid)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()


def find_user_mysql(userid):
    finduser = []
    sql = """select * from usertable where id = '%d';""" %(userid)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    for i in cursor.fetchall():
        finduser.extend(list(i))

    return finduser


def update_user_mysql(attr,new,userid):
    sql = """update usertable set %s = '%s' where id = '%d';""" % (attr,new,userid)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()




