# -*- coding: utf-8 -*-
import math
import os
import sys
import datetime
from apps.utils import date
from apps.utils import db, file
from apps.utils.msg import *
from apps.utils.file import ReadConfigFile, WriteExcel
from apps.utils.fmt import PrintTable


# 增加用户信息
def add():
    userinfo = InputMsg("请输入你要增加的用户信息 [姓名 年龄 手机 地址，以空格格开]：").split()
    if len(userinfo) != 4:
        return "你输入的信息不全！", False
    else:
        sql = '''INSERT INTO auth_user(username, age, tel, address, create_time, update_time) VALUES('{}', {}, '{}', '{}', from_unixtime({}), from_unixtime({}));'''.format(
            *userinfo, date.CurrentTimestamp(), date.CurrentTimestamp())
        return db.Insert(sql)


# 删除用户信息
def delete():
    uid = InputMsg("请输入你要删除的用户ID: ")
    if uid.isdigit():
        sql = '''delete from auth_user where id = {};'''.format(uid)
        return db.Delete(sql)
    else:
        return "输入的用户ID错误，必须为数字！", False


# 更改用户信息
def update():
    uid = InputMsg("请输入你要修改的用户ID: ")
    if uid.isdigit():
        res, ok = find(id=uid)
        if ok:
            whereDic = InputMsg("请输入你要更改的用户信息[ 字段名1=字段值1, 字段名2=字段值2, ... ]: ")
            whereDic = ','.join(["{}='{}'".format(x.split('=')[0].strip(), x.split('=')[1].strip()) for x in whereDic.split(',')])

            # 更新对应数据，未更新修改时间
            # sql = 'UPDATE auth_user SET {} WHERE id = {};'.format(whereDic, uid)
            # 更新对应数据，同时更新修改时间
            sql = 'UPDATE auth_user SET {}'.format(whereDic) + ' ,update_time=from_unixtime({}) '.format(date.CurrentTimestamp()) + 'WHERE id = {};'.format(uid)

            return db.Update(sql)
        else:
            return "不存在该用户！", False
    else:
        return "输入的用户ID错误，必须为数字！", False


# 查询用户信息
def find(id=''):
    if id:
        uid = id
    else:
        uid = InputMsg("请输入你要修改的用户ID: ")

    if uid.isdigit():
        fields = ['id', 'username', 'age', 'tel', 'address', 'create_time', 'update_time']
        sql = 'SELECT {} FROM auth_user WHERE id = {};'.format(','.join(fields), uid)
        msg, ok = db.Select(sql)
        if not ok:
            return msg, False
        dataMsg = [dict(zip(fields, x)) for x in msg]
        responseMsg, _ = PrintTable(dataMsg)
        SuccMsg(responseMsg)
        return '', True
    else:
        return "输入的用户ID错误，必须为数字！", False


# 查询所有用户信息，增加show参数，如果是在保存成excel文件或输出到网页的时候不PrintTable用户信息
def findall(show=True):
    fields = ['id', 'username', 'age', 'tel', 'address', 'create_time', 'update_time']
    sql = 'SELECT {} FROM auth_user;'.format(','.join(fields))
    # SuccMsg(sql)
    msg, ok = db.Select(sql)
    if not ok:
        return msg, False
    dataMsg = [dict(zip(fields, x)) for x in msg]
    responseMsg, _ = PrintTable(dataMsg)
    if show:
        SuccMsg(responseMsg)

    # 查询时不在控制台显示返回结果
    if show:
        return '', True
    else:
        return dataMsg, True


# 保存用户信息至Excel
def excel():
    BASEDIR = os.path.dirname(os.path.abspath(__file__))
    excel_options, ok = ReadConfigFile(os.path.join(BASEDIR, '..', 'conf.ini'), 'EXCEL')

    if not ok:
        errmsg = excel_options
        return errmsg, False

    EXCEL_NAME = excel_options.get('excel_name')

    res, ok = findall(show=False)

    if ok:
        msg, ok = WriteExcel(EXCEL_NAME, res)
        if ok:
            return msg, True
        else:
            return msg, False
    else:
        return '保存不成功', False


# 退出操作
def quit():
    SuccMsg("正在保存数据至excel文件！")
    excel()
    SuccMsg("正在退出系统！")
    sys.exit(0)

# 选择操作函数
def LogicOper():
    prompt = "\n操作选项: \n\tadd\n\tdelete\n\tupdate\n\tfind\n\tfindall\n\texcel\n\tquit\n请输入您的操作:  "
    mapFunc = {'add': add, 'delete': delete, 'update': update, 'find': find, 'findall': findall, 'excel': excel, 'quit': quit}

    while 1:
        op = InputMsg(prompt)
        try:
            msg, ok = mapFunc[op]()
            if not ok:
                WarnMsg(msg)
            else:
                SuccMsg(msg)
        except KeyError as e:
            WarnMsg("不存在输入的操作，请重试！")
        except Exception as e:
            WarnMsg(e.args)



