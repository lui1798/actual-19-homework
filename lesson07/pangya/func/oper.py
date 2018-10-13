# 导入模块
import logging
import pymysql
import configparser
import sys
import os
import jinja2
import json

import db
from fmt import PrintTable


'''获取uid'''


def list_uid():
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute('select * from mgt;')
    uid_list = []
    for x in cursor.fetchall():
        uid_list.append(x[0])
    return uid_list
    cursor.close()
    conn.close()


'''添加用户信息'''


def add():
    body = input("输入添加用户的名字、电话、地址和年龄,以空格隔开（如wangli 18822888888 beijing 11）：")
    user_list = body.split(' ')
    if len(user_list) != 4:
        logging.warning("你添加的用户信息格式错误")
    else:
        name, tel, address, age = user_list
        has_error = False
        if not tel.isdigit():
            logging.warning("电话号码不是数字")
            has_error = True
        elif not age.isdigit():
            logging.warning("年龄不是数字")
            has_error = True
        if not has_error:
            uid_list = list_uid()
            uid = max(uid_list + [0]) + 1
            user_list.insert(0, uid)
            user_list[4] = int(user_list[4])
            insert_sql = "insert into mgt(uid,name,age,tel,address) values({},'{}','{}','{}',{})".format(*user_list)
            db.Execute_db(insert_sql)


# if __name__ == '__main__':
#     add_users()


'''修改指定用户信息'''


def update():
    uid = input("请输入修改用户ID:")
    is_exists = False
    if uid.isdigit():
        uid_list = list_uid()
        if int(uid) in uid_list:
            is_exists = True
        else:
            logging.warning("ID错误")
    if is_exists:
        body = input("请输入更新类型和更新信息，用空格隔开（如 age 28）:")
        user_update = body.split(' ')
        if len(user_update) == 2:
            if user_update[0] == 'age':
                if user_update[1].isdigit():
                    user_update[1] = int(user_update[1])
                    update_sql = "update mgt set {}='{}' where uid={}".format(*user_update, uid)
                    db.Execute_db(update_sql)
                else:
                    logging.warning("年龄输入错误")
            else:
                update_sql = "update mgt set {}='{}' where uid={}".format(*user_update, uid)
                db.Execute_db(update_sql)
        else:
            logging.warning("输入错误")


'''删除'''


def delete():
    uid = input("请输入你要删除用户的ID：")
    if uid.isdigit():
        delete_sql = "delete from mgt where uid = {};".format(uid)
        db.Execute_db(delete_sql)
        logging.info("该用户删除成功")
    else:
        logging.warning("输入错误")


# if __name__ == '__main__':
#     delete_users()



'''查找'''


def find():
    text = input("请输入查找信息: ")
    fields = ['uid', 'name', 'age', 'tel', 'address']
    if text.isdigit():
        find_sql = ''' select * from mgt where uid={}  or age= {};'''.format(text, text)
    else:
        find_sql = ''' select * from mgt where name='{}' or address ='{}'or tel ='{}';'''.format(text, text, text)
    msg, ok = db.Select(find_sql)
    if not ok:
        return 'Select failed', False
    dataMsg = [dict(zip(fields, x)) for x in msg]
    if dataMsg == []:
        print("无该信息")
    else:
        responseMsg, _ = PrintTable(dataMsg)
        print(responseMsg)
        return '', True


def list():
    fields = ['uid', 'name', 'age', 'tel', 'address']
    sql = 'SELECT {} FROM mgt;'.format(','.join(fields))
    logging.debug(sql)
    msg, ok = db.Select(sql)
    if not ok:
        return 'Select failed', False
    dataMsg = [dict(zip(fields, x)) for x in msg]
    if dataMsg == []:
        print("当前列表为空")
    else:
        responseMsg, _ = PrintTable(dataMsg)
        print(responseMsg)
    return '', True




def quit():
    sys.exit(-1)


def format():
    format = input("Please input format[ html | csv]: ")
    if format.strip() == "html":
        print(1)
        TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "templates")
        print(TEMPLATE_DIR)
        template_loader = jinja2.FileSystemLoader(searchpath=TEMPLATE_DIR)
        print(2)
        template_env = jinja2.Environment(loader=template_loader)
        print(3)
        try:
            template = template_env.get_template("users.html")
        except Exception as e:
            print(e.args)
            return
        print(0)
        fields = ['uid', 'name', 'age', 'tel', 'address']
        sql = 'SELECT {} FROM auth_user;'.format(','.join(fields))
        msg, ok = db.Select(sql)
        print(msg)
        if not ok:
            print("Select failed")
        else:
            dataMsg = [dict(zip(fields, x)) for x in msg]
            content = {'fields': fields, 'content': dataMsg}
            html_str = template.render(content)
            print("22")
            print(html_str)
            print("11")


    elif format == "csv":
        print("csv")
    else:
        print("not support")

def LogicOper():
    prompt = "\n\t可选项:add/update/find/list/format/quit:\n\t请输入操作选项:  "
    mapFunc = {
        'add': add,
        'delete': delete,
        'update': update,
        'find': find,
        'list': list,
        'quit': quit,
        'format': format,
    }

    while True:

        op = input(prompt).strip()
        try:
            mapFunc[op]()
        except Exception as e:
            logging.warning("无效选项，重新输入：")
