#coding: utf-8
'''
用户管理系统
1.登陆验证（管理员：admin / 123123），如果用户连续输错三次密码便锁定一分钟
2.登陆成功后，加载系统已存在的用户信息
3.对用户进行操作
    3.1查询并分页展示用户（支持用户名、电话、地址搜索，每页展示4条记录，通过输入页数来切换页码）
    3.2添加用户（如果添加用户名重复，则报错）
    3.3删除用户（如果删除用户不存在，则报错）
    3.4保存用户到文件中
    3.5退出（自动保存）
    3.6其他指令提示无效

'''
#导入涉及的模块

import time
import json
import math
import getpass
import logging

#定义常量
MAX_LOGIN_TIMES = 3             #用户、密码最大输入次数
USER_NAME = "admin"             #管理员用户名
USER_PASSWORD = "123123"        #管理员用户密码
LOCK_TIME = 60                  #锁定时间设置为60秒
PAGE_EACH = 4                   #每页打印数量
PRINT_TITLE = "|{name:<15}|{age:<5}|{tel:<14}|{address:<20}|{id:<4}|"       #打印表头
FORMAT_ARGS = {'name':'name','age':'age','tel':'tel','address':'address','id':'id'}     #格式化打印参数
LOG_LEVEL = logging.DEBUG        #日记级别

#定义变量
userlist = []
logging.basicConfig(level=LOG_LEVEL,
                    filename = "log.txt",
                    filemode = "a",
                    format='%(asctime)s - %(filename)s[%(funcName)s] - %(levelname)s: %(message)s')

#各功能模块
def login():
    #登陆用户名及密码检验，如果输入三次错误返回falseaaa
    login_times = 0
    while True:
        user_name = input("please input username:")
        user_password = getpass.getpass("please input password:")
        if user_name.strip() == USER_NAME and user_password.strip() == USER_PASSWORD:
            return True
        else:
            print("用户或密码输入错误！")
            login_times = login_times +1
            logging.error("用户密码输错{}次".format(login_times))
            print("还有{}次机会！！！".format(MAX_LOGIN_TIMES-login_times))
        if login_times == MAX_LOGIN_TIMES:
            print("用户锁定中，请稍后再试！")
            logging.critical("密码输错三次，用户锁定！")
            return False

def login_lock():
    #锁定用户
    login_time = time.time()
    ff = open("locktime","w")
    ff.write(json.dumps(login_time))
    ff.close()


def lock_check():
    #检查用户是否锁定
    ff = open("locktime","r")
    membu = ff.read()
    unlock_time = float(json.loads(membu)) + LOCK_TIME
    ff.close()
    if time.time() > unlock_time:
        return True
    else:
        return False


def load_userinfo():
    #加载用户信息
    ff = open("users","r")
    membu = ff.read()
    ff.close()
    return json.loads(membu)


def user_add(userlist):
    #用户信息添加
    logging.debug("将进行用户增加操作...")
    user_str = input("请输入用户信息（姓名 年龄 电话 地址）:")
    user_add_list = user_str.split()

    if len(user_add_list) !=4:
        print("输入信息有误")
        return userlist
    elif  not user_add_list[1].isdigit() or not user_add_list[2].isdigit() :
        print("输入年龄或电话有误")
        return userlist
    else:
        name = user_add_list[0]
        age = int(user_add_list[1])
        tel = user_add_list[2]
        address = user_add_list[3]
        max_id = max(x["id"] for x in userlist)
        id = max_id + 1
        userlist.append({
            "name": name,
            "age": age,
            "tel": tel,
            "address": address,
            "id": id
        })
        print("用户{}新增成功".format(name))
        logging.warning("用户({})新增成功".format(name))
        return userlist


def user_print(userlist):
    #用户信息打印
    logging.debug("将进行用户打印操作...")
    while True:
        max_page = math.ceil(len(userlist) / float(PAGE_EACH))
        try:
            page_print = int(input("\n\n\033[31m一共{}页，请输入打印的页码（输入9999退出）：\033[0m".format(max_page)))
            if page_print == 9999:
                break

            if page_print > max_page:
                print("输入页码超出范围，请重新输入！")
                continue

            print(PRINT_TITLE.format(**FORMAT_ARGS))
            print("-" * 64)
            for x in userlist[(page_print - 1) * PAGE_EACH:page_print * PAGE_EACH]:
                print(PRINT_TITLE.format(**x))
            logging.debug("打印全部用户信息成功！！！")
        except Exception as e:
            print("指令输入有误!", e)
            logging.warning("打印指令输入有误！！！")

def user_query(userlist):
    #根据名字、电话、地址搜索用户信息
    logging.debug("将进行用户查询、打印操作...")
    query_str = input("请输入要查询的名字、电话或地址：")
    query_list = []
    for x in userlist:
        if x["name"] ==query_str or x["tel"] == query_str or x["address"] ==query_str:
            query_list.append(x)
    logging.debug("查询{}成功，返回数据！！！".format(query_str))
    return query_list

def user_delete(userlist):
    #删除用户信息
    logging.debug("将进行用户删除操作...")
    try:
        delete_id = int(input("请输入删除的用户id:"))
        for x in userlist:
            if x["id"] == delete_id:
                userlist.remove(x)
                print("{} 删除成功".format(x))
                logging.warning("用户({})删除成功！！！".format(x["name"]))
                return userlist
    except Exception as e:
        print("输入的id有误!!")
        logging.warning("id输入错误，退出delete！！！")
        return userlist

def user_update(userlist):
    #修改用户信息
    logging.debug("将进行用户更新操作...")
    id_str = input("请输入修改信息的用户编号：")
    if  id_str.isdigit() and int(id_str) in [x['id'] for x in userlist]:
        for y in userlist:
            if y["id"] == int(id_str):
                print("用户原信息为：{}".format(y))
                user_str = input("请输入用户新信息（姓名 年龄 电话 地址）:")
                userlist.remove(y)
                user_add_list = user_str.split()
                name = user_add_list[0]
                age = int(user_add_list[1])
                tel = user_add_list[2]
                address = user_add_list[3]
                userlist.append({
                    "name": name,
                    "age": age,
                    "tel": tel,
                    "address": address,
                    "id": int(id_str)
                })
                print("用户信息修改成功！")
                logging.warning("用户({})更新成功！！！".format(name))
                return userlist
    else:
        print("输入的用户编号有误！")
        logging.warning("更新时用户编号输入错误！！！")
        return userlist

def user_save(userlist):
    #保存用户信息
    logging.debug("将进行用户保存操作...")
    ff = open("users","w")
    membu = json.dumps(userlist)
    ff.write(membu)
    ff.close()
    print("用户信息保存成功")

##############################################################################

def user_main():
    logging.info("-------------系统开启------------")
    if lock_check():
        if login():
            print("\033[31m----------------------登陆成功------------------------\033[0m")
            logging.info("用户admin登陆成功")
        else:
            login_lock()
            exit()
    else:
        print("用户锁定中，请稍后再试！")
        logging.warning("登陆失败，用户锁定")
        exit()

    userlist = load_userinfo()
    print(userlist)
    while True:
        print("\033[31m请输入操作：\n","\033[34madd   ->添加\n","query ->查询\n","update->修改\n",
                               "delete->删除\n","print ->打印\n","exit  ->退出系统\n","save  ->保存")
        op = input("please input your option:\033[0m").strip()
        if op == "add":
            userlist = user_add(userlist)
        elif op == "query":
            query_list = user_query(userlist)
            user_print(query_list)
        elif op == "print":
            user_print(userlist)
        elif op == "update":
            userlist = user_update(userlist)
        elif op == "delete":
            userlist = user_delete(userlist)
        elif op == "save":
            user_save(userlist)
        elif op == "exit":
            user_save(userlist)
            print("\033[31m--------------------退出系统成功------------------------\033[0m")
            logging.info("退出系统！！！")
            break
        else:
            print("输入指令无效，请重新输入！")
            logging.warning("错误指令")

#调用主函数
if __name__=="__main__":
    user_main()
