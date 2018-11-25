
import os
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
sys.path.append(BASE_DIR)

# from libs.dbutils import db as pydb


from libs import dbutils


host = "127.0.0.1"
user = "root"
password = "123456"
port = 3306
database = "python19"


db = dbutils.db(host, user, password, database, port)

'''
sql = "show databases;"
msg = db.show_database_nums(sql)
print(msg)
'''


sql = 'SELECT * FROM users;'
result = db.select(sql)
for line in result:
    print(line)


