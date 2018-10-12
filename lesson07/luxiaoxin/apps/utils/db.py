#encoding: utf-8
#-----导入内置模块--------
import traceback
#-----导入开源模块--------
import pymysql
#-----导入自定义模块--------


#-----定义公用常量-------
#MySQL数据连接参数
PARAMS = {
      'host':'127.0.0.1',
      'port':3306,
      'user':'root',
      'passwd':'Netscout1!',
      'db':'reboot19',
      'charset':'utf8'
    }
#MySQL执行语句常量
SQL_SELECT = ''' SELECT id,name,age,tel,address FROM user'''
SQL_ADD = ''' INSERT INTO user(id,name,age,tel,address) VALUES(%s, %s, %s, %s, %s)'''
SQL_DELETE =''' DELETE  FROM user WHERE id=%s'''
SQL_MODIFY =''' UPDATE user SET name=%s, age=%s, tel=%s, address=%s WHERE id=%s'''

#--------定义功能函数-------
#连接数据库函数
def connect():
    conn = pymysql.connect(**PARAMS)
    return conn


#执行SQL语句函数
def execute_sql(sql, args=(), fetch=True, one=False):
    cnt, result = 0, None
    conn = connect()
    cur = None
    try:
        cur = conn.cursor()
        cnt = cur.execute(sql, args)
        if fetch:
            result = cur.fetchone() if one else cur.fetchall()
        else:
            conn.commit()

    except BaseException as e:
        print(e)
        print(traceback.format_exc())
    finally:
        if cur:
            cur.close()

    return cnt, result


#查询数据函数
def Select():
    cnt, result = execute_sql(SQL_SELECT)
    return cnt, result


#添加数据函数
def Insert(*args):
    cnt, result = execute_sql(SQL_ADD, args, fetch=False)
    return cnt, result



#修改数据函数
def Modify(*args):
    cnt, result = execute_sql(SQL_MODIFY, args, fetch=False)
    return cnt, result


#删除数据函数
def Delete(data):
    cnt, result = execute_sql(SQL_DELETE, (data,), fetch=False)
    return cnt, result
