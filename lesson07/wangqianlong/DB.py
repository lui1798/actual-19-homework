import pymysql

from utils import ReadConfigFile

'如要创建表，表结构如下：'
'''
CREATE_TABLE = """CREATE TABLE USERINFO (
         uid  INT(10) NOT NULL INCREAMENT,
         name  CHAR(20),
         age INT(10),  
         tel INT(20),
         address CHAR(20));"""

'''


# 连接数据库
def Connect(CONFIGFILE2):
    try:
        config, ok = ReadConfigFile(CONFIGFILE2, 'DB1')
        # print('1111111',config)
        db = pymysql.connect(**dict(config))
    except Exception as e:
        print(e)
        return 'connect error', False
    else:
        return db, True

'''
# 创建数据库
def Create_database(DATABASE):
    db, flag = Connect()
    if flag:
        try:
            # 创建游标，通过连接与数据通信
            cursor = db.cursor()
            # 执行sql语句
            cursor.execute('show databases;')
            rows = cursor.fetchall()
            for row in rows:
                tmp = "%2s" % row
                # 判断数据库是否存在
                if DATABASE == tmp:
                    flag = True
                    break
            if not flag:
                cursor.execute('create database ' + DATABASE + ';')
                # 提交到数据库执行
                db.commit()
        except Exception as e:
            print(e)
        finally:
            # 关闭数据库连接
            db.close()


# 创建表
def Create_table(DATABASE, CREATE_TABLE):
    db, flag = Connect()
    if flag:
        try:
            databse_use = 'use ' + DATABASE + ';'
            cursor = db.cursor()
            cursor.execute(databse_use)
            cursor.execute(CREATE_TABLE)
        except Exception as e:
            print(e)
        finally:
            db.close()
'''


# 查询
def Select(CONFIGFILE2, selet_sql):
    users = []
    db, flag = Connect(CONFIGFILE2)
    if flag:
        try:
            cursor = db.cursor()
            cursor.execute(selet_sql)
            for x in cursor.fetchall():
                users.append(x)
            db.commit()
            cursor.close()
            return users, flag
            # print(users)
        except Exception as e:
            print(e)
            return users, False
        finally:
            db.close()
    else:
        return users, False


# 增加
def Insert(CONFIGFILE2, insert_sql):
    db, flag = Connect(CONFIGFILE2)
    if flag:
        try:
            cursor = db.cursor()
            cursor.execute(insert_sql)
            db.commit()
            cursor.close()
            return ' ', flag
        except Exception as e:
            print(e)
            return 'error', False
        finally:
            db.close()
    else:
        return 'insertfailed', False


# 修改
def Update(CONFIGFILE2,update_sql):
    db, flag = Connect(CONFIGFILE2)
    if flag:
        try:
            cursor = db.cursor()
            cursor.execute(update_sql)
            db.commit()
            cursor.close()
            return ' ', True
        except Exception as e:
            print(e)
            return 'error', False
        finally:
            db.close()
    else:
        return 'updatafailed', False


# 删除
def Delete(CONFIGFILE2,delete_sql):
    db, flag = Connect(CONFIGFILE2)
    if flag:
        try:
            cursor = db.cursor()
            cursor.execute(delete_sql)
            db.commit()
            cursor.close()
            return ' ', True
        except Exception as e:
            print(e)
            return 'error', False
        finally:
            db.close()
    else:
        return 'deletefailed', False
