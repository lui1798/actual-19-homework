#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/16 上午12:06
# @Author  : LuoFeng
# @Site    : 
# @File    : db.py
# @Software: PyCharm

import configparser as conf
import pymysql as mysql

# 加载数据库配置文件
config = conf.ConfigParser()
config.read('../config.ini')

# 数据连接配置
host = config['MYSQL']['HOST']
user = config['MYSQL']['USER']
password = config['MYSQL']['PASSWORD']
database = config['MYSQL']['DATABASE']

class DB(object):
    def _get_db_conn_(self):
        try:
            conn = mysql.connect(host=host, user=user, password=password, db=database)
        except Exception as e:
            print("数据库连接异常", e)

    def _exec_sql_(self, sql):
        conn = self._get_db_conn_()
        cursor = conn.cursor()
        result = True

        try:
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
            result = False
        finally:
            conn.close()
            return result


    def insert(self, sql):
        return self._exec_sql_(sql)

    def delete(self, sql):
        return self._exec_sql_(sql)

    def update(self, sql):
        return self._exec_sql_(sql)


    def select(self, sql):
        conn = self._get_db_conn_()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            conn.commit()

        except Exception as e:
            print(e)
        finally:
            conn.close()

