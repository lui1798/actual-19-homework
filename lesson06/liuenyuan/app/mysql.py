#!/usr/bin/env python3
import pymysql
#import config 
from config import readconfig
def connect(sql,operation):
    mysql  = readconfig('mysql')
    host   = mysql['host']
    port   = mysql['port']
    name   = mysql['name']
    user   = mysql['user']
    passwd = mysql['passwd']
    # 打开数据库连接
    db= pymysql.connect(host=host,user=user,password=passwd,db=name,port=port)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
     
    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute(sql)
    if operation == "add":
       db.commit()
    elif operation == "delete":
       pass
    elif operation == "change":
       db.commit()
    elif operation == "find":
       result = cursor.fetchall()
       return result
    else:
       pass
    # 使用 fetchone() 方法获取单条数据.
    # 关闭数据库连接
    db.close()
if __name__ == '__main__' :
    #sql = """insert into user(name,passwd,qq,server,failed_time) values ('zhangsan','123',123234124,'123214',3)"""
    sql  = """select UNIX_TIMESTAMP(login_time) from user where name = 'zhangsan'"""
    result = connect(sql,'find')
    print(result)
