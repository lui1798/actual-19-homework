#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/14 下午4:57
# @Author  : iteemo
# @File    : dbtool.py
import traceback
import pymysql


class mysqlutils(object):
    def __init__(self, **kwargs):
        try:
            # self._conn = pymysql.connect(host=kwargs["host"], user=kwargs["user"], password=kwargs["password"],
            self._conn = pymysql.connect(cursorclass=pymysql.cursors.DictCursor, **kwargs)
            self.__cursor = None
        except Exception as err:
            print('mysql连接错误：' + err)
    def __del__(self):
        if (self._conn):
            self._conn.close()

    def queryone(self, sql, param=None):
        con = self._conn
        cur = con.cursor()

        row = None
        try:
            cur.execute(sql, param)
            row = cur.fetchone()
        except Exception as e:
            # 如果失败回滚当前事物
            con.rollback()
            print(e)
        finally:
            cur.close()
            return self.simple_value(row)

    def queryall(self, sql, param=None):
        con = self._conn
        cur = con.cursor()

        rows = None
        try:
            cur.execute(sql, param)
            rows = cur.fetchall()
        except Exception as e:
            con.rollback()
            print(e)
        finally:
            cur.close()
            return self.simple_list(rows)

    def insertone(self, sql, param=None):

        con = self._conn
        cur = con.cursor()

        lastrowid = 0
        try:
            cur.execute(sql, param)
            con.commit()
            lastrowid = cur.lastrowid
        except Exception as e:
            con.rollback()
            print(e)
        finally:
            cur.close()
            return lastrowid

    def execute(self, sql, param=None):
        con = self._conn
        cur = con.cursor()

        cnt = 0
        try:
            cnt = cur.execute(sql, param)
            con.commit()
        except Exception as e:
            con.rollback()
            print(e)
        finally:
            cur.close()
            #con.close()
            return cnt

    def simple_list(self, rows):
        if not rows:
            return rows

        if len(rows[0].keys()) == 1:
            simple_list = []
            # print(rows[0].keys())
            key = list(rows[0].keys())[0]
            for row in rows:
                simple_list.append(row[key])
            return simple_list

        return rows

    def simple_value(self, row):
        if not row:
            return None
        if len(row.keys()) == 1:
            key = list(row.keys())[0]
            return row[key]

        return row
