import os
import pymysql
from utils.file import ReadConfig
from utils.print_msg import *


# 连接数据库
def Connect():
    # 获取当前目录
    BASEDIR = os.path.dirname(os.path.abspath(__file__))
    try:
        db_options, ok = ReadConfig(os.path.join(BASEDIR, '..', 'conf.ini'), 'DB')
    except Exception as e:
        return

    db_options['port'] = int(db_options['port'])

    try:
        conn = pymysql.Connect(**db_options)
        cur = conn.cursor()
        return conn, cur, '', ok
    except Exception as e:
        return '', '', e.args, False



# 查询数据库
def Select(sql, conn, cur):
    try:
        cur.execute(sql)
        res = cur.fetchall()
    except Exception as e:
        return e.args, conn, cur, False

    return res, conn, cur, True


def Insert(sql, conn, cur):
    try:
        cur.execute(sql)
    except Exception as e:
        conn.rollback()
        return e.args, conn, cur, False

    return '', conn, cur, True


def Update(sql, conn, cur):
    try:
        cur.execute(sql)
    except Exception as e:
        conn.rollback()
        return e.args, conn, cur, False
    if cur.rowcount == 1:
        return '', conn, cur, True


def Delete(sql, conn, cur):
    try:
        cur.execute(sql)
    except Exception as e:
        conn.rollback()
        return e.args, conn, cur, False
    if cur.rowcount == 1:
        return '', conn, cur, True


def Commit(conn, cur):
    conn.commit()
    return conn, cur


def Close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()
