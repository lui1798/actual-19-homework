import configparser
import base64
import pymysql
import output_log

config = configparser.ConfigParser()
config.read('conf.ini')

def open_mysql():
    server_ip = config['MYSQL']['server_ip']
    user = str(base64.urlsafe_b64decode(config['MYSQL']['user']), encoding='utf-8')
    passwd = str(base64.urlsafe_b64decode(config['MYSQL']['passwd']), encoding='utf-8')
    db = pymysql.connect(server_ip, user, passwd, "USERMESSAGE")
    mysqldb = db.cursor()
    output_log.log_log('debug','连接数据库了')
    return db,mysqldb

def execute_mysql(mysqldb,sql):
    mysqldb.execute(sql)

def commit_mysql(db):
    db.commit()

def rollback_mysql(db):
    db.rollback()

def close_mysql(db,mysqldb):
    mysqldb.close()
    db.close()

