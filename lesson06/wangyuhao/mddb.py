#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time          : 2018/9/16 上午12:08
# Author        : Yuhao.Wang
# FileName      : mddb.py
# Description   : 
#
import pymysql
from mdconfig import ReadConfig

mysql_host = ReadConfig('config.ini', 'MYSQL', 'HOST')
mysql_user = ReadConfig('config.ini', 'MYSQL', 'USER')
mysql_pass = ReadConfig('config.ini', 'MYSQL', 'PASSWORD')
mysql_db   = ReadConfig('config.ini', 'MYSQL', 'DATABASE')
mysql_port = ReadConfig('config.ini', 'MYSQL', 'PORT')

conn = pymysql.connect(host=mysql_host, user=mysql_user, password=mysql_pass, database=mysql_db, port=int(mysql_port))

# def excute_sql_read(sql):
#     try:
#         conn = pymysql.connect(host=mysql_host, user=mysql_user, password=mysql_pass, database=mysql_db, port=int(mysql_port))
#         cursor = conn.cursor()
#         cursor.execute(sql)
#         data = cursor.fetchall()






def list_user_mysql():
    user_list = []
    sql = 'select * from usertable;'
    cursor = conn.cursor()

    for info in cursor.fetchall():
        user_dict = {}
        user_dict['id'] = info[0]
        user_dict['name'] = info[1]
        user_dict['age'] = info[2]
        user_dict['tel'] = info[3]
        user_dict['add'] = info[4]
        user_list.append(user_dict)

    return user_list

def user_id_mysql():
    user_id_list = []
    sql = 'select id from usertable'
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

    for id in cursor.fetchall():
        user_id_list.append(int(id[0]))

    return user_id_list

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
    conn.close()
