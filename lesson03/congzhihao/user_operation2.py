# coding=utf-8
"""
用户管理系统：
list    显示正常用户
add     新增用户
update  修改用户信息
delete  删除用户
find    查询某个用户信息
exit    退出系统

"""
#####################################################################
import json
import datetime

# userlist:存放系统用户数据
userlist = []

# 加载本地数据
try:
    f2 = open("userlog.db", "r")
    data = f2.read()
    userlist = json.loads(data)
    f2.close()
    print("用户信息加载成功！！！")
except FileNotFoundError:
    print("本地用户信息未加载！！！")

# 加载上次输入三次密码错误时间
f2 = open("timelog.db",'r')
membur = f2.read()
t = json.loads(membur)
t0 = datetime.datetime.strptime(t,"%Y-%m-%d %H:%M:%S")
f2.close()

# 管理员用户名及密码
user = ("admin","123456")
ntime = 3
tt = datetime.datetime.now()
'''
1.先提示用户输入密码
2.如果输入错误，总次数减1，并继续输入
3.如果三次输入错误，记录"当前时间+ 1day"并存储到变量t0中，并把t0写入文件，同时关闭程序。
4.用户再次打开程序时，系统读取t0中的值，如果tnow>t0,则继续执行用户密码输入；如果tnow<=t0,则关闭程序
5.重置日期请运行"time_reset.py"
'''

# 用户操作
if tt <= t0 :
    print("user locked,please try 24 hours later!!!")
    exit()

while True:
    user_name = input("please input your name:")
    user_password = input("please input your password:")
    try:
        if user_name.strip() == user[0] and user_password.strip() == user[1]:
            print("login in successfully")
            break
        else:
            ntime = ntime -1
            print("name or password wrong!")
            print("{} times left".format(ntime))
            if ntime == 0:
                tnow = datetime.datetime.now() +datetime.timedelta(days =1)
                f3 = open("timelog.db","w")
                memburr = json.dumps(tnow.strftime("%Y-%m-%d %H:%M:%S"))
                f3.write(memburr)
                f3.close()
                exit()
    except TypeError:
        print("输入格式有误")

while True:
    print("\033[34m\"list\" (:to list all user) \033[0m")
    print("\033[34m\"add\" (:to add user)\033[0m ")
    print("\033[34m\"update\" (:to update user information)\033[0m")
    print("\033[34m\"delete\" (:to delete user information)\033[0m")
    print("\033[34m\"find\" (:to find certain user information)\033[0m")
    print("\033[34m\"exit\" (:to quit)\033[0m")
    op = input('\033[34m please input action: \033[0m')

    if op == 'list':
        for i in range(0, len(userlist), 4):
            print("-----------------page{}&total page{}------------------".format(i // 4 + 1, (len(userlist)-1)// 4 + 1))
            print("id\tname\tage\ttel\taddress\t".expandtabs(12))
            for u in userlist[i:i + 4]:
                print("{}\t{}\t{}\t{}\t{}".format(u["id"], u["name"], u["age"], u["tel"], u["address"]).expandtabs(12))
            print("-----------------------------------------------------")

    elif op == 'add':
        max_index = 0
        for x in userlist:
            if max_index < int(x["id"]):
                max_index = int(x["id"])
        new_user = {}
        new_user["id"] =max_index +1
        new_user["name"] = input("please input user name:")
        new_user["age"] = input("please input user age:")
        new_user["tel"] = input("please input user tel:")
        new_user["address"] = input("please input user address:")
        userlist.append(new_user)
        print("--user information add successfully!!!--")

    elif op == 'update':

        user_id = int(input("--please input an id to update:"))
        new_name = input("please input user name:")
        new_age = input("please input user age:")
        new_tel = input("please input user tel:")
        new_address = input("please input user address:")
        # 先获取此id对应的index，然后对此index 重新赋值
        for x in userlist:
            if x["id"] == user_id:
                x["name"] = new_name
                x["age"] = new_age
                x["tel"] = new_tel
                x["address"] = new_address
                print("id:{} update successfully")
            else:
                print("id: {} fail")
    elif op == 'delete':

        user_id = int(input("--please input an id to update:"))
        for x in userlist:
            if x["id"] == user_id:
                user_del = userlist.pop(userlist.index(x))
        print("{} delete successfully!!".format(user_del))

    elif op == 'find':
        user_info = input("please input user id or name:")
        for x in userlist:
            try:
                user_info = int(user_info)
                if x["id"] == user_info:
                    print("user information: {}".format(x))
            except ValueError:
                if x["name"] == user_info:
                    print("user information: {}".format(x))


    elif op == 'exit':
        break

    else:
        print("\033[31m invalid cmd!!!\033[0m")  # 加上颜色 警告信息

print("\033[32m Login out\033[0m")
print("\033[32m ------------------------------------\033[0m")

# 将userlist写入到txt文件中###
