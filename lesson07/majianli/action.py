import logging
from dbconnect import conn_db
import csv
import  configparser
from prettytable  import PrettyTable

#日志输出
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                    filename='access.log',
                    filemode='a'
                    )

def query():
    try:
        sql = 'select * from user_list;'
        data = conn_db(sql)
        studo = PrettyTable()
        studo.field_names = ['id', 'name', 'age', 'tel', 'adress', 'creaet_time', 'update_time']
        for i in data:
            studo.add_row(i)
        print(studo)
    except Exception as e:
        print(e)

def add():
    try:
        userinfor = input('输入添加的用户信息(format：name age tel addr):').split()
        if len(userinfor) != 4:
            print('参数个数不对，请重新输入')
            logging.warning('参数个数不对')
        else:
            sql = "insert into user_list (name,age,tel,addr) values ('{}',{},'{}','{}')".format(userinfor[0],int(userinfor[1]),userinfor[2],userinfor[3])
            conn_db(sql)
            logging.debug('用户{}添加成功。用户信息name = {},age = {},tel = {}, addr = {}'.format(userinfor[0],userinfor[0],int(userinfor[1]),userinfor[2],userinfor[3]))
    except Exception as e:
        print(e)

def select():
    try:
        username = input('输入你要查找的用户：').strip()
        sql = "select * from user_list where name = '{}'".format(username)
        data = conn_db(sql)
        if data == ():
            print('无此用户，请重新输入')
        else:
            studo = PrettyTable()
            studo.field_names = ['id', 'name', 'age', 'tel', 'adress', 'creaet_time', 'update_time']
            for i in data:
                studo.add_row(i)
            print(studo)
    except Exception as e:
        print(e)

def delete():
    try:
        userinfo = input('输入你要删除的用户：').strip()
        sql = "delete from user_list where name = '{}'".format(userinfo)
        conn_db(sql)
    except Exception as e:
        print(e)

def update():
    try:
        userinfo = input('输入你要修改的用户：').strip()
        update_info = input('输入你要修改的用户信息(age|tel|addr|name)：').strip()
        value = input('输入值:').strip()
        sql = "update  user_list set {} = '{}'  where name = '{}'".format(update_info,value,userinfo)
        conn_db(sql)
    except Exception as e:
        print(e)

def dump_csv():
    try:
        sql = 'select * from user_list;'
        data = conn_db(sql)
        csvFile = open("test.csv", 'w', newline='')
        writer = csv.writer(csvFile)
        writer.writerow(('id', 'name', 'age', 'tel', 'addr', 'create_time', 'update_time'))
        for i in data:
            writer.writerow((i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        csvFile.close()
        print('导出cvs文件成功。')
    except Exception as e:
        print(e)

def config():
    try:
        conf_keys = input('要查看关键字(LOG|DB|CSV|HTML):')
        cf = configparser.ConfigParser()  # 实例化对象
        cf.read('config.conf')  # 读取配置文件
        # sec = cf.sections()    # 读取头文件 返回列表
        # opts = cf.options('DB')  # 读取头文件下的属性，返回列表
        # kv = cf.items('DB')  # 读取头文件为DB下的所有，每行已元组返回，全部已列表返回
        kv = cf.items('{}'.format(conf_keys))
        for i in kv:
            print(i)
    except Exception as e:
        print(e)
