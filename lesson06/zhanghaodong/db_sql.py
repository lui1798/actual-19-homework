#!/usr/local/bin/python3
# mail:haodongz@yeah.net
# _*_ coding:utf-8 _*_
import pymysql

db = pymysql.connect(host='162.218.211.185', user='test', password='testdb123!', database='test', port=3306)

selet_sql = 'select  * from userinfo;'

cursor = db.cursor()

'''查询'''
cursor = db.cursor()

cursor.execute(selet_sql)
for x in cursor.fetchall():
    print(x)
'''写入'''
insert_sql = "insert into userinfo(userinfo_id,userinfo_name,userinfo_add,userinfo_phone,userinfo_age) values ('5','haodongz','beijing','186xx','28');"
cursor.execute(insert_sql)
db.commit()
'''修改'''
up_sql = ''' 
update userinfo set userinfo_name='51reboot' where userinfo_id = '1';
 '''
cursor.execute(up_sql)
db.commit()

'''删除'''
del_sql = '''
delete  from     userinfo where       userinfo_id = '1';  
'''
cursor.execute(del_sql)
db.commit()


'''关闭'''

cursor.close()
db.cursor()


