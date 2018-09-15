# -*- coding: utf-8 -*-
import math
from lock import *
from utils import db, file
from utils.print_msg import *


# 增加用户信息函数
def AddUser(conn, cur):
    user = InputMsg("请输入你要增加的用户信息 [姓名 年龄 手机 地址，以空格格开]：").split()
    if len(user) != 4:
        WarnMsg("你输入的信息有误！")
    else:
        username, age, tel, address = user
        has_error = False
        if not age.isdigit():
            WarnMsg("输入的年龄错误，必须为数字！")
            has_error = True
        if not has_error:
            # sql = '''insert into user(username, age, tel, address) values("{}", {}, "{}", "{}");'''.format(username, age, tel, address)
            sql = '''insert into user(username, age, tel, address) values("%s", "%s", "%s", "%s");''' %(username, age, tel, address)
            rs, conn, cur, ok = db.Insert(sql, conn, cur)
            if not ok:
                WarnMsg(rs)
                return conn, cur

            SuccMsg("添加用户信息成功！")
    return conn, cur


# 删除用户信息函数
def DelUser(conn, cur):
    has_error = False
    try:
        id = int(InputMsg("请输入你要删除的用户的ID: "))
    except Exception as e:
        WarnMsg("输入的用户ID错误，必须为数字！")
        has_error = True
    if not has_error:
        sql = '''delete from user where id = {};'''.format(id)
        res, conn, cur, ok = db.Delete(sql, conn, cur)
        if ok:
            SuccMsg("删除用户成功！")
        else:
            WarnMsg("输入的用户ID不存在！")
    return conn, cur


# 修改用户信息函数
def ModifyUser(conn, cur):
    id = InputMsg("请输入你要修改的用户的ID：")
    if id.isdigit():
        id = int(id)

    sql = "select * from user where id = {};".format(id)
    res, conn, cur, ok = db.Delete(sql, conn, cur)

    if ok:
        user = InputMsg("请输入你要增加的用户信息 [姓名 年龄 手机 地址，以空格格开]：").split()
        if len(user) != 4:
            WarnMsg("你输入的信息有误！")
        else:
            username, age, tel, address = user
            has_error = False
            if not age.isdigit():
                has_error = True
                WarnMsg("输入的年龄错误，必须为数字！")

            if not has_error:
                sql = '''update user set username = "{}", age = {}, tel = "{}", address = "{}" where id = {};'''.format(username, age, tel, address, id)
                conn = db.Update(sql, conn, cur)
                SuccMsg("用户信息更新成功！")
    else:
        WarnMsg("输入的用户ID不存在！")
    return conn, cur


# 查询用户信息函数
def QueryUser(conn, cur):
    BASEDIR = os.path.dirname(os.path.abspath(__file__))
    try:
        page_options, ok = config.ReadConfig(os.path.join(BASEDIR, 'conf.ini'), 'PAGE')
    except Exception as e:
        return

    PAGE_SIZE = int(page_options['page_size'])

    data = InputMsg("请输入要查询的内容，可以是用户名、电话、地址，回车查询所有：")
    if not data:
        sql = "SELECT * FROM user;"
    else:
        sql = '''SELECT * FROM user WHERE username="{0}" OR tel="{0}" OR address="{0}"'''.format(data)
    users, conn, cur, ok = db.Select(sql, conn, cur)
    if not ok:
        WarnMsg(users)
        return

    fields = ['id', 'username', 'age', 'tel', 'address']
    users = [dict(zip(fields, x)) for x in users]

    users_find_count = len(users)
    if users_find_count == 0:
        SuccMsg("暂无用户相关信息！")
        return conn, cur
    elif users_find_count <= PAGE_SIZE:
        PrintUsers(users)
        return conn, cur
    else:
        max_page = math.ceil(users_find_count / PAGE_SIZE)
        while True:
            page_num = InputMsg("用户信息共有{0}页，请输入查询页码[1 ~ {0}]，按q键则返回上级菜单:".format(max_page)).strip().lower()
            if page_num.isdigit() and int(page_num) <= max_page:
                page_num = int(page_num)
                PrintUsers(users[(page_num - 1) * PAGE_SIZE : page_num * PAGE_SIZE])
            elif page_num == 'q':
                SuccMsg("返回上级菜单！")
                return conn, cur
            else:
                WarnMsg("你输入的页码错误！")
                return conn, cur


# 保存用户信息函数
def SaveUser(conn, cur):
    db.Commit(conn, cur)
    SuccMsg("成功保存用户信息！")
    return conn, cur


# 保存用户信息至xls
def SaveExcel(conn, cur):
    BASEDIR = os.path.dirname(os.path.abspath(__file__))
    try:
        login_options, ok = config.ReadConfig(os.path.join(BASEDIR, 'conf.ini'), 'EXCEL')
    except Exception as e:
        return

    EXCEL_NAME = login_options['excel_name']

    sql = "select * from user;"
    users, conn, cur, ok = db.Select(sql, conn, cur)
    if not ok:
        WarnMsg(users)
        return
    file.Write_Excel(EXCEL_NAME, users)
    SuccMsg("成功保存用户信息至xls文件！")
    return conn, cur


# 选择操作函数
def operate(conn, cur):
    while True:
        op = InputMsg("请输入相关操作[add, del, mod, que, save, excel, exit]：")
        if op == "add":
            conn, cur = AddUser(conn, cur)
        elif op == "del":
            conn, cur = DelUser(conn, cur)
        elif op == "modify":
            conn, cur = ModifyUser(conn, cur)
        elif op == "query":
            conn, cur = QueryUser(conn, cur)
        elif op == "save":
            conn, cur = SaveUser(conn, cur)
        elif op == "excel":
            conn, cur = SaveExcel(conn, cur)
        elif op == "exit":
            SaveUser(conn, cur)
            SaveExcel(conn, cur)
            db.Close(conn, cur)
            SuccMsg("正在退出系统！")
            break
        else:
            WarnMsg("不存在你输入的相关操作！")