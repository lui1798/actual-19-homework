import pymysql
import logging
import xlwt
import math
import os


"""连接sql数据库，返回"""

def ConnectSql(host,port,user,passwd,database):
    conn = pymysql.connect(host=host,
                           port=port,
                           user=user,
                           passwd=passwd,
                           db=database)
    cur = conn.cursor()
    return conn, cur


def CreateMysql(cur):
    cur.execute(u"create database congzhihao;")
    cur.execute(u"use congzhihao;")
    print("database:congzhihao 创建成功")


def InitSql(cur):
    try:
        cur.execute(
            u"create table users(id int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT, name char(20),age char(4),tel char(12),address char(30));")
        cur.execute(u"insert into users (name,age,tel,address) values('xiaoming','22','15588681111','beijing'); ")
        cur.execute(u"insert into users (name,age,tel,address) values('xiaohong','21','15588681112','beijing'); ")
        cur.execute(u"insert into users (name,age,tel,address) values('xiaohua','22','15588681113','shanghai'); ")
        cur.execute(u"insert into users (name,age,tel,address) values('kobe','39','15588681114','chicago'); ")
        cur.execute(u"insert into users (name,age,tel,address) values('magic','44','15588681115','chicago'); ")
        cur.execute(u"insert into users (name,age,tel,address) values('jordan','55','15588681116','chicago'); ")
        print("初始化数据库成功")

    except:
        print("数据库已存在，继续")


def SelectUser(conn,print_title,format_args,page_each):
    logging.debug("将进行用户查询、打印操作...")
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    query_str = input("请输入要查询的名字、电话或地址(直接回车查询全部)：")
    if query_str == "":
        num = cur.execute("select * from users;")
    else:
        num = cur.execute(
            "select * from users where name='%s' or tel='%s' or address='%s'" % (query_str, query_str, query_str))
    if num == 0:
        print("查询无数据")
    else:
        user_info = cur.fetchall()
        logging.debug("查询{}成功，返回{}数据！！！".format(query_str, num))
        logging.debug("将进行用户打印操作...")
        max_page = math.ceil(num / float(page_each))
        while True:
            try:
                page_print = int(input("\n\n\033[31m一共{}页，请输入打印的页码（输入9999退出）：\033[0m".format(max_page)))

                if page_print == 9999:
                    break

                if page_print > max_page:
                    print("输入页码超出范围，请重新输入！")
                    continue

                print(print_title.format(**format_args))
                print("-" * 64)

                for x in user_info[(page_print - 1) * page_each:page_print * page_each]:
                    print(print_title.format(**x))

                logging.debug("打印全部用户信息成功！！！")

            except Exception as e:
                print("指令输入有误!", e)
                logging.warning("打印指令输入有误！！！")


def InsertUser(cur, conn):
    logging.debug("将进行用户增加操作...")
    user_str = input("请输入用户信息（姓名 年龄 电话 地址）:")
    user_add_list = user_str.split()

    if len(user_add_list) != 4:
        print("输入信息有误，请重新操作")
        return

    elif not user_add_list[1].isdigit() or not user_add_list[2].isdigit():
        print("输入年龄或电话有误")
        return

    else:
        name = user_add_list[0]
        age = int(user_add_list[1])
        tel = user_add_list[2]
        address = user_add_list[3]

        try:
            cur.execute(
                "insert into users (name,age,tel,address) values ('%s','%s','%s','%s')" % (name, age, tel, address))
            conn.commit()
            print("用户{}新增成功".format(name))
            logging.info("用户({})新增成功".format(name))

        except:
            print("插入失败")
            logging.info("用户新增操作失败")


def UpdateUser(cur, conn):
    logging.debug("将进行用户更新操作...")
    id_str = input("请输入修改信息的用户编号：")
    if id_str.isdigit():
        id = int(id_str)
        num = cur.execute("select * from users where id='%s';" % (id))
        if num == 1:
            print("用户原信息为：{}".format(cur.fetchall()))
            user_str = input("请输入用户新信息（姓名 年龄 电话 地址）:")
            user_add_list = user_str.split()
            name = user_add_list[0]
            age = int(user_add_list[1])
            tel = user_add_list[2]
            address = user_add_list[3]
            num = cur.execute("update users set  name='%s',age='%s',tel='%s',address='%s' where id='%s'" % (
                name, age, tel, address, id))
            conn.commit()
            if num == 0:
                print("输入新信息有误，用户更新失败")
            else:
                print("id:%s用户信息更新成功" % id)
                logging.warning("用户({})更新成功！！！".format(name))
    else:
        print("输入的用户编号有误！")
        logging.warning("更新时用户编号输入错误！！！")


def DeleteUser(cur, conn):
    logging.debug("将进行用户删除操作...")
    id = input("请输入删除的用户id:")
    if id.isdigit() and cur.execute("select * from users where id='%s';" % (int(id))):
        num = cur.execute("delete from users where id='%s'" % (id))
        if num == 0:
            print("删除失败")
        else:
            conn.commit()
            print("id:%s用户信息删除成功" % id)
            logging.warning("id:%s用户信息删除成功" % id)
    else:
        print("输入的id有误!!")
        logging.warning("id输入错误，退出delete！！！")


def ExpertUser(cur):
    logging.debug("导出excel文件操作")
    num = cur.execute("select * from users;")
    if num == 0:
        print("无用户数据，导出失败")
        logging.warning("无用户数据，导出失败")
    else:
        user_info = cur.fetchall()
        wbk = xlwt.Workbook()
        sheet1 = wbk.add_sheet("users")
        sheet1.write(0, 0, "id")
        sheet1.write(0, 1, "name")
        sheet1.write(0, 2, "age")
        sheet1.write(0, 3, "tel")
        sheet1.write(0, 4, "address")

        for i in range(num):
            for j in range(5):
                sheet1.write(i+1,j,user_info[i][j])

        wbk.save("user-information.xls")
        print("导出成功，文件位于{}".format(os.getcwd()+"/user-information.xls"))
        logging.info("excel文件导出成功！")