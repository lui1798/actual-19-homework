import os
import pymysql
from apps.utils.file import ReadConfigFile


def connect():
	BASEDIR = os.path.dirname(os.path.abspath(__file__))
	dbinfo, ok = ReadConfigFile(os.path.join(BASEDIR, '..', '..', 'config.ini'), 'DB')
	if not ok:
		return 'pymysql connect failed.', False
	return pymysql.connect(**dict(dbinfo)), True

'''查询数据'''
def Select(sql):
	conn, ok = connect()
	if not ok:
		errmsg = conn
		return errmsg, False
	
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
	
'''写入数据'''
def Insert(sql):
	conn, ok = connect()
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
	return '', True

'''更新数据'''
def Update(sql):
	conn, ok = connect()
	if not ok:
		errmsg = conn
		return errmsg, False
	
	cur = conn.cursor()
	
	try:
		cur.execute(sql)
		conn.commit()
		print(cur.rowcount)
		if cur.rowcount == 1:
			return "", True
	except Exception as e:
		conn.rollback()
		return e.args, False
	finally:
		cur.close()
		conn.close()

'''删除数据'''
def Delete(sql):
	conn, ok = connect()
	if not ok:
		errmsg = conn
		return errmsg, False
	
	cur = conn.cursor()
	
	try:
		cur.execute(sql)
		conn.commit()
		if cur.rowcount == 1:
			return "", True
		else:
			return "Delete failed.", False
	except Exception as e:
		conn.rollback()
		return e.args, False
	finally:
		cur.close()
		conn.close()