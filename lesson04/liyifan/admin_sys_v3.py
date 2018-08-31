#扩展：1.每次删除，删除信息之后的信息序号都-1，例如，删除3，序号4变3，序号5变4

#导入模块
import datetime
import getpass
import json
import math

#定义常量
LOCK_FILE = "lock"
LOCK_DURATION = datetime.timedelta(seconds=20)

LOGIN_USERNAME = "admin"
LOGIN_PWD = "123456"

USER_FILE = "user.json"
MAX_COUNTS = 3

USER_INFO_NUM = 4

PAGE_SIZE = 2
TABLE_TPL = '{id:^10}|{name:^10}|{age:^5}|{tel:^15}|{address:^15}'
TABLE_SPLIT_LINE = 59
TABLE_TITLE = {"id" : "id", "name" : "name","age" : "age","tel" : "tel","address":"address"}

#定义公共变量
#--------------def形式--------------#
#1.check检查是否锁定
def is_unlock():
    try:
        #文件存在
        fd = open(LOCK_FILE)
        locktime_type_str = fd.read()
        fd.close()  # 如果不关闭……
        locktime_type_date = datetime.datetime.strptime(locktime_type_str,'%Y-%m-%d %H:%M:%S')
        is_unlock = datetime.datetime.now() - locktime_type_date > LOCK_DURATION
        #locktime_type_str.strptime 错误原因：字符串没有strptime方法
    except:
        is_unlock = True

    return is_unlock

#2.用户登录（前提：未锁定）
def is_login():
    is_login = False
    for i in range(MAX_COUNTS):
        username = input("请输入用户名： ")
        pwd = input("请输入密码： ")

        if LOGIN_USERNAME == username and LOGIN_PWD == pwd:
            is_login = True #将is_login的布尔值作为登录开关
            break

        if i == MAX_COUNTS - 1:
            print("您的用户已锁定，请稍后再试")
        else:
            print("您的输入有误，请重新输入")
    return is_login

#3-1.登录成功，加载用户
def get_users(users):
    try:
        fd = open(USER_FILE)
        users_info_str = fd.read()
        fd.close()
        users = json.loads(users_info_str)
    except:
        pass
    return users

def list_all(users):
    if len(users) == 0:
        print("目前尚无信息")
    else:
        max_page = math.ceil(len(users) / PAGE_SIZE)
        print(TABLE_TPL.format(**TABLE_TITLE))
        print('-' * TABLE_SPLIT_LINE)
        for user in users:
            print(TABLE_TPL.format(**user))

#操作_add
def users_add(users):
    is_add_error = False
    print("**  add 操作  **")
    name = input("请输入您的姓名： ")
    age = input("请输入您的年龄： ")
    tel = input("请输入您的电话(*11位数字)： ")
    address = input("请输入您的地址： ")
    user_info_str = f"{name} {age} {tel} {address}"
    user_info = user_info_str.split()
    if len(user_info) != USER_INFO_NUM or \
        not age.isdigit() or \
        not tel.isdigit() or \
        len(tel) != 11:
        is_add_error = True

    if is_add_error:
        print("输入错误")
    else:
        name, age, tel, address = user_info    #解包
        id = max([x.get("id") for x in users] + [0]) + 1    #若没有找到id，则max输出0
        #列表使用max函数： max([2] , [3])   结果输出[3]
        #                 max([2] + [3])  结果输出3
        user = {
            "id":id,
            "name":name,
            "age":age,
            "tel":tel,
            "address":address
        }
        users.append(user)
        print("您的以下信息添加成功: ")
        print(user)
    return users

#delete
def users_delete(users):
    is_del_error = False
    print("**  delete 操作  **")
    try:
        del_index = int(input("请输入您要删除的id序号： "))
        for user in users:
            if del_index == user.get("id"):
                users.remove(user)
                user_info = user
                is_del_error = True
                for x in users:
                    if del_index < x.get("id"):
                        x['id'] = int(x['id']) - 1
                break
    except:
        is_del_error = False

    if is_del_error:
        print(f"删除成功，您删除的信息为： {user}")
    else:
        print("输入错误")
    return users

#modify
def users_modify(users):
    is_modify_exists = False
    print("**  modify 操作  **")
    modify_id = input("请输入要修改的用户id: ")
    #id输入是否正确的对应 输出走向
    try:
        for user in users:
            if int(modify_id) == user.get("id"):
                is_modify_exists = True
                user_up = user
                break
    except:
            is_modify_exists = False
    #id输入正确
    if is_modify_exists:
        #用户录入信息是否正确
        is_error = False
        print("您要更新的用户信息为：" , user_up)
        modify_text = input("请依次输入用户信息（用户名/年龄/电话(*11位数字)/地址） 并使用空格分割： ")
        modify_text_list = modify_text.split()
        name, age, tel, address = modify_text_list

        if len(modify_text_list) != USER_INFO_NUM or\
            not age.isdigit() or\
            not tel.isdigit() or\
            len(tel) != 11:
            is_error = True
        #录入错误
        if is_error:
            print("用户信息输入错误")
        #录入正确
        if not is_error:
            user_up["name"] = name
            user_up["age"] = age
            user_up["tel"] = tel
            user_up["address"] = address
            print(f"更新成功，修改后的用户信息为：{user_up}")
    #id输入错误
    else:
        print("id输入错误")
    return users

#list
def users_list(users):
    print("**  list 操作  **")
    txt = input("请输入要查询的关键词：")
    #查询字典中的value
    users_find = []
    for user in users:
        for value in user.values():
            #由于id号为int类型，需要加str转换
            if str(txt) in str(value):
                users_find.append(user)

    users_find_count = len(users_find)
    if users_find_count == 0:
        print("查询结果：无")
    #字典格式化输出
    elif users_find_count <= PAGE_SIZE:
        print(TABLE_TPL.format(**TABLE_TITLE)) #打印title
        print('-' * TABLE_SPLIT_LINE)
        for user in users_find:
            print(TABLE_TPL.format(**user))
    #分页
    else:
        max_page = math.ceil(users_find_count / PAGE_SIZE)
    #输入页码 1<查错（非数字/不存在页码） ；  2<正确（打印）
        while True:
            find_page_num = input(f"您好，共有{max_page}页符合，请输入您要查询的页码('q'键退出):")
            if find_page_num.isdigit() and int(find_page_num) <= max_page:
                page_num = int(find_page_num)
                print(TABLE_TPL.format(**TABLE_TITLE))
                print('-' * TABLE_SPLIT_LINE)
                # print(user)
                for user in users_find[(page_num - 1) * PAGE_SIZE : page_num * PAGE_SIZE]:
                    print(TABLE_TPL.format(**user))
            elif find_page_num == 'q':
                break
            else:
                print("输入错误")
                break
    return users

#save
def users_save(users):
    print("**  save 操作  **")
    fd = open(USER_FILE, 'w')
    fd.write(json.dumps(users))
    fd.close
    print("保存成功")

def users_exit(users):
    print("**  exit 操作  **")
    #保存，不保存，取消操作
    quit_op = input("程序即将退出，是否保存？（y/是  n/否  其他/取消）")
    if quit_op == 'y':
        fd = open(USER_FILE, 'w')
        fd.write(json.dumps(users))
        fd.close
        exit()
    elif quit_op == 'n':
        exit()
    else:
        pass
    return users

def option(users):
    while True:
        op = input("请输入操作对应的数字(add:1 / delete:2 / modify:3 / list_find:4 / list_all:5 /save:6 / exit:q)")
        if op == '1':
            users_add(users)
        elif op == '2':
            users_delete(users)
        elif op == '3':
            users_modify(users)
        elif op == '4':
            users_list(users)
        elif op == '6':
            users_save(users)
        elif op == 'q':
            users_exit(users)
        elif op == '5':
             list_all(users)
        else:
            print("输入错误")

def lock_user():
        fd = open(LOCK_FILE, 'w')
        locktime_type_date = datetime.datetime.now()
        locktime_type_str = locktime_type_date.strftime('%Y-%m-%d %H:%M:%S')
        fd.write(locktime_type_str)
        fd.close()

def main():
    #check检查：不锁定
    users = []
    if not is_unlock():
        print("用户锁定")
    if is_unlock():
        #不锁定，用户登录
        if is_login():
            #登录成功，加载用户
            users = get_users(users)
            #加载成功，用户操作
            option(users)
        #不锁定，登录失败
        else:
            #4.登录失败
            lock_user()

main()




#--------------非def形式--------------#
#1.check检查是否锁定
# try:
#     fd = open(LOCK_FILE)
#     locktime_type_str = fd.read()
#     fd.close()  # 如果不关闭……
#     locktime_type_date = datetime.datetime.strptime(locktime_type_str,'%Y-%m-%d %H:%M:%S')
#     is_unlock = datetime.datetime.now() - locktime_type_date > LOCK_DURATION
#     #locktime_type_str.strptime 错误原因：字符串没有strptime方法
# except:
#     is_unlock = True
# #2.用户登录（前提：未锁定）
# if is_unlock:
#     for i in range(MAX_COUNTS):
#         username = input("请输入用户名： ")
#         pwd = input("请输入密码： ")
#
#         if LOGIN_USERNAME == username and LOGIN_PWD == pwd:
#             is_login = True #将is_login的布尔值作为登录开关
#             break
#
#         if i == MAX_COUNTS - 1:
#             print("您的用户已锁定，请稍后再试")
#         else:
#             print("您的输入有误，请重新输入")
#     #3.用户操作(前提：登录成功）
#     if is_login:
#         #3-1.登录成功，加载用户
#         try:
#             fd = open(USER_FILE)
#             users_info_str = fd.read()
#             fd.close()
#             users = json.loads(users_info_str)
#         except:
#             pass
#
#         while True:
#             op = input("请输入操作对应的数字(add:1 / delete:2 / modify:3 / list:4 / save:5 / exit:q)")
#             #3-1-1.add(1)
#             if op == '1':
#                 print("**  add 操作  **")
#                 name = input("请输入您的姓名： ")
#                 age = input("请输入您的年龄： ")
#                 tel = input("请输入您的电话(*11位数字)： ")
#                 address = input("请输入您的地址： ")
#                 user_info_str = f"{name} {age} {tel} {address}"
#                 user_info = user_info_str.split()
#                 if len(user_info) != USER_INFO_NUM or \
#                     not age.isdigit() or \
#                     not tel.isdigit() or \
#                     len(tel) != 11:
#                     is_add_error = True
#
#                 if is_add_error:
#                     print("输入错误")
#                 else:
#                     name, age, tel, address = user_info    #解包
#                     id = max([x.get("id") for x in users] + [0]) + 1    #若没有找到id，则max输出0
#                     #列表使用max函数： max([2] , [3])   结果输出[3]
#                     #                 max([2] + [3])  结果输出3
#                     user = {
#                         "id":id,
#                         "name":name,
#                         "age":age,
#                         "tel":tel,
#                         "address":address
#                     }
#                     users.append(user)
#                     print("您的以下信息添加成功: ")
#                     print(user)
#             #3-2.delete(2)
#             elif op == '2':
#                 print("**  delete 操作  **")
#                 try:
#                     del_index = int(input("请输入您要删除的id序号： "))
#                     for user in users:
#                         if del_index == user.get("id"):
#                             users.remove(user)
#                             user_info = user
#                             is_del_error = True
#                             break
#                 except:
#                     is_del_error = False
#
#                 if is_del_error:
#                     print(f"删除成功，您删除的信息为： {user}")
#                 else:
#                     print("输入错误")
#             #3-3.modify(3)
#             elif op == '3':
#                 print("**  modify 操作  **")
#                 modify_id = input("请输入要修改的用户id: ")
#                 #id输入是否正确的对应 输出走向
#                 try:
#                     for user in users:
#                         if int(modify_id) == user.get("id"):
#                             is_modify_exists = True
#                             user_up = user
#                             break
#                 except:
#                         is_modify_exists = False
#                 #id输入正确
#                 if is_modify_exists:
#                     #用户录入信息是否正确
#                     is_error = False
#                     print("您要更新的用户信息为：" , user_up)
#                     modify_text = input("请依次输入用户信息（用户名/年龄/电话/地址） 并使用空格分割： ")
#                     modify_text_list = modify_text.split()
#                     name, age, tel, address = modify_text_list
#
#                     if len(modify_text_list) != USER_INFO_NUM or\
#                         not age.isdigit() or\
#                         not tel.isdigit():
#                         is_error = True
#                     #录入错误
#                     if is_error:
#                         print("用户信息输入错误")
#                     #录入正确
#                     if not is_error:
#                         user_up["name"] = name
#                         user_up["age"] = age
#                         user_up["tel"] = tel
#                         user_up["address"] = address
#                         print(f"更新成功，修改后的用户信息为：{user_up}")
#                 #id输入错误
#                 else:
#                     print("id输入错误")
#             #3-4.list(4)
#             elif op == '4':
#                 print("**  list 操作  **")
#                 txt = input("请输入要查询的关键词：")
#                 #查询字典中的value
#                 users_find = []
#                 for user in users:
#                     for value in user.values():
#                         #由于id号为int类型，需要加str转换
#                         if str(txt) in str(value):
#                             users_find.append(user)
#
#                 users_find_count = len(users_find)
#                 if users_find_count == 0:
#                     print("查询结果：无")
#                 #字典格式化输出
#                 elif users_find_count <= PAGE_SIZE:
#                     print(TABLE_TPL.format(**TABLE_TITLE)) #打印title
#                     print('-' * TABLE_SPLIT_LINE)
#                     for user in users_find:
#                         print(TABLE_TPL.format(**user))
#                 #分页
#                 else:
#                     max_page = math.ceil(users_find_count / PAGE_SIZE)
#                 #输入页码 1<查错（非数字/不存在页码） ；  2<正确（打印）
#                     while True:
#                         find_page_num = input(f"您好，共有{max_page}页符合，请输入您要查询的页码('q'键退出):")
#                         if find_page_num.isdigit() and int(find_page_num) <= max_page:
#                             page_num = int(find_page_num)
#                             print(TABLE_TPL.format(**TABLE_TITLE))
#                             print('-' * TABLE_SPLIT_LINE)
#                             # print(user)
#                             for user in users_find[(page_num - 1) * PAGE_SIZE : page_num * PAGE_SIZE]:
#                                 print(TABLE_TPL.format(**user))
#                         elif find_page_num == 'q':
#                             break
#                         else:
#                             print("输入错误")
#                             break
#             #3-5.save(5)
#             elif op == '5':
#                 print("**  save 操作  **")
#                 fd = open(USER_FILE, 'w')
#                 fd.write(json.dumps(users))
#                 fd.close
#                 print("保存成功")
#             #3-6.exit(q)
#             elif op == 'q':
#                 print("**  exit 操作  **")
#                 #保存，不保存，取消操作
#                 quit_op = input("程序即将退出，是否保存？（y/是  n/否  其他/取消）")
#                 if quit_op == 'y':
#                     fd = open(USER_FILE, 'w')
#                     fd.write(json.dumps(users))
#                     fd.close
#                     break
#                 elif quit_op == 'n':
#                     break
#                 else:
#                     pass
#             else:
#                 print("输入错误，请重新输入")
#     else:
#         #3-2.登录失败，写入锁定时间
#         fd = open(LOCK_FILE, 'w')
#         locktime_type_date = datetime.datetime.now()
#         locktime_type_str = locktime_type_date.strftime('%Y-%m-%d %H:%M:%S')
#         fd.write(locktime_type_str)
#         fd.close()
# else:
#     print("您的用户已锁定，请稍后再试")
