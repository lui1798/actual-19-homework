import pymysql
import os
# import file
from file import ReadConfigFile


def connect_db():
	BASEDIR = os.path.dirname(os.path.abspath(__file__))
	dbinfo, ok = ReadConfigFile(os.path.join(BASEDIR, 'config.ini'), 'CONNECT')
	if not ok:
		return '数据库连接失败'
	return pymysql.connect(**dbinfo)


'''创建表'''
def Create_table():
    conn = connect_db()
    cursor = conn.cursor()
    sql="create table mgt(uid int,name varchar(32),age int,tel varchar(32),address varchar(32)); "
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

'''判断表mgt是否存在，为空时创建表mgt'''
def is_table_mgt():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("show tables like 'mgt'")
    if cursor.fetchall() == ():
        Create_table()

'''提交到数据库'''
def Execute_db(sql):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


'''查询数据'''
def Select(sql):
    conn= connect_db()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
        return rows, True
    except Exception as e:
        return e.args, False
    finally:
        cur.close()
        conn.close()




