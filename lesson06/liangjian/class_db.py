import logging
import pymysql
import math

users = []
USER_INFO_NUM = 4

class MySQL(object):
    def __init__(self, host, port, user, passwd, db, table):
        self.host = host
        self.port = port
        self.user = user
        self.password = passwd
        self.db = db
        self.table = table

    def connectMysql(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.password,db=self.db)
            self.cursor = self.conn.cursor()
            print('connect ' + self.table + ' correctly!')
        except:
            print('connect mysql error.')

    def queryMysql(self):
        sql = "SELECT * FROM " + self.table
        try:
            print("query Mysql:")
            self.cursor.execute(sql)
            for d in self.cursor:
                print(d)
        except:
           print(sql + ' execute failed.')

    def insertMysql(self):
        text = input("请依次输入用户信息(用户名, 年龄, 电话号码, 地址), 信息使用空格分割:")
        user = text.split()
        if len(user) != USER_INFO_NUM:
            print("输入数据不正确")
        else:
            name, age, tel, address = user
            has_error = False
        if not age.isdigit():
            print("年龄输入有问题")
            has_error = True

        if not tel.isdigit():
            print("电话号码有问题")
            has_error = True

        if not has_error:


            sql = '''insert into user_info(name,age,tel,address) values("%s","%s","%s","%s"); '''%(name,age,tel,address)
            try:
                print("insert Mysql:")
                self.cursor.execute(sql)
                self.conn.commit()
                print(sql)
                print("添加用户成功")  
            except Exception as e:
                print(e)
                print("insert failed.")

    def updateMysqlSN(self):
        text = input("请输入修改用户ID:")
        is_exists = False
        uid = 0
        if text.isdigit():
            uid = int(text)
            conn = self.connectMysql()
            selet_sql = 'select * from user_info;'
            self.cursor.execute(selet_sql)
            for x in  self.cursor.fetchall():
                if uid == list(x)[0]:
                    print("更新用户信息:",x)
                    is_exists = True
                    break

        if is_exists:
            text = input("请依次输入用户信息(用户名, 年龄, 电话号码, 地址), 信息使用空格分割:")
            user = text.split()
            if len(user) != USER_INFO_NUM:
                print("输入数据不正确")
            else:
                name, age, tel, address = user
                has_error = False
                if not age.isdigit():
                    has_error = True
                    print("输入的年龄不正确")

                if not tel.isdigit():
                    has_error = True
                    print("输入的电话不正确")

                if not has_error:
                    #self.cursor = connect.cursor()
                    selet_sql = 'select * from user_info;'
                    self.cursor.execute(selet_sql)

                    for x in self.cursor.fetchall():
                        if uid == list(x)[0]:
                            print(list(x)[0])
                            update_sql  = '''  update user_info set name="%s",age="%s",tel="%s",address="%s" where id = "%d";'''%(name,age,tel,address,uid)
                            self.cursor.execute(update_sql)
                            self.conn.commit()
                            self.cursor.close()
                            self.conn.close()

                            print("更新成功")
                            break
        else:
            print("输出ID错误")

    def deleteMysql(self):  # 删除
        text = input("请输入要删除的ID: ")
        if text.isdigit():
            uid = int(text)
            conn = pymysql.connect("140.143.227.246","test","d^7^34lE","test")
            cursor = conn.cursor()
            selet_sql = 'select id from user_info;'
            cursor = conn.cursor()
            cursor.execute(selet_sql)
        
            for x in cursor.fetchall():
               # print(list(x)[0])
                if uid == list(x)[0]:
                    delete_sql = '''   delete from user_info where id = "%d";'''%uid
                    cursor.execute(delete_sql)
                    conn.commit()
                    cursor.close()
                    conn.close()


                    print("删除用户成功")
                    break

            else:
               print("输入ID错误")
        else:
            print("输入ID错误")

    def closeMysql(self):
        self.conn.commit()  # 不执行此句，所作的操作不会写入到数据库中
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    comysql = MySQL(host='140.143.227.246', user='test', passwd='d^7^34lE', db='test', port=3306, table='user_info')
    comysql.connectMysql()
   # comysql.queryMysql()
   # comysql.insertMysql()
    # comysql.queryMysql()
    comysql.deleteMysql()
    # comysql.queryMysql()
   # comysql.updateMysqlSN()
    # comysql.queryMysql()
    # comysql.closeMysql()

