
'''
    练习：
        通过类的方式 实现对数据库基本的操作
            增、删、改查


    PyMySQL

    1. pip install pymysql
    2. 导入
    3. 创建连接
    4. 创建游标
    5. 拼接sql
    6. 执行
    7. 结果 返回
    8. 关闭游标 和 关闭连接

'''

import pymysql
import pymysql.cursors




class db(object):

    def __init__(self, host=None, user=None, password="", database=None, port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

        self.cursor = self.connect()


    def connect(self):
        try:
            dbconn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                db=self.database,
                port = self.port,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            return dbconn.cursor()
        except Exception as e:
            return None


    def insert(self, sql):
        self.cursor.execute(sql)


    def show_database_nums(self, sql):
        return self.cursor.execute(sql)


    def select(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result



