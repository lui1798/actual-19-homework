import os
import pymysql
from apps.utils.file import ReadConfigFile
from apps.utils.msg import *


# 连接数据库
def Connect():
    # 获取当前目录
    BASEDIR = os.path.dirname(os.path.abspath(__file__))
    db_options, ok = ReadConfigFile(os.path.join(BASEDIR, '..', '..', 'conf.ini'), 'DB')

    if not ok:
        errmsg = db_options
        return errmsg, False

    db_options['port'] = int(db_options['port'])
    return pymysql.connect(**dict(db_options)), True


# 查询数据库
def Select(sql):
    conn, ok = Connect()
    if not ok:
        errmsg = conn
        return errmsg, False

    cur = conn.cursor()
    try:
        cur.execute(sql)
        res = cur.fetchall()
        if cur.rowcount >= 1:
            return res, True
        else:
            return '没有你要查询的数据！', False
    except Exception as e:
        return e.args, False
    finally:
        cur.close()
        conn.close()


def Insert(sql):
    conn, ok = Connect()
    if not ok:
        errmsg = conn
        return errmsg, False

    cur = conn.cursor()

    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        return e.args, False
    finally:
        cur.close()
        conn.close()
    return '数据插入成功！', True


def Update(sql):
    conn, ok = Connect()
    if not ok:
        errmsg = conn
        return errmsg, False

    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        if cur.rowcount == 1:
            return '数据更新成功！', True
    except Exception as e:
        conn.rollback()
        return e.args, False
    finally:
        cur.close()
        conn.close()


def Delete(sql):
    conn, ok = Connect()
    if not ok:
        errmsg = conn
        return errmsg, False

    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        if cur.rowcount == 1:
            return '数据删除成功！', True
    except Exception as e:
        conn.rollback()
        return e.args, False
    finally:
        cur.close()
        conn.close()
