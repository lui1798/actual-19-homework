
import pymysql


'''
pymysql.connect(*args, **kwargs)

:param host: Host where the database server is located
:param user: Username to log in as
:param password: Password to use.
:param database: Database to use, None to not use a particular one.
:param port: MySQL port to use, default is usually OK. (default: 3306)
'''
conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='python19', port=3306)
# print(dir(db_handler))

# conn.autocommit(True)

selet_sql = 'select * from mgt;'

# conn = db_handler.connect_wxremit_db()
cursor = conn.cursor()

'''查询'''
cursor.execute(selet_sql)
for x in cursor.fetchall():
    print(x)



'''写入'''
insert_sql = '''
insert into mgt(uid, name, age, tel, address) values('4', 'monkey4', '19', '192xxx', 'beijing');
'''
cursor.execute(insert_sql)
conn.commit()


'''修改'''
update_sql = '''
update mgt set name='51reboot' where uid = '4';
'''
cursor.execute(update_sql)
conn.commit()


'''删除'''
delete_sql = '''
delete from mgt where uid = '1';
'''
cursor.execute(delete_sql)
conn.commit()

''''关闭'''
cursor.close()
conn.close()
