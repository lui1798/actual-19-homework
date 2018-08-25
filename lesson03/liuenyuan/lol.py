#!/usr/bin/env python3
import json
import  getpass
import hashlib
import time
#添加用户
def add():
    with open("mysql.txt", "r+") as f:
        file = f.read()
        data = json.loads(file)
    print("""欢迎注册（请输入用户名、密码、qq号、所在服务区）
        eg:   zhangsan   123   123  艾欧尼亚    
        """)
    while True:
        flag = False
        while True:
            name = input(""" 输入你的用户名,不允许为空:""").strip()
            if name == "q" or name == "Q":
                print("退出！！！回到主页面")
                flag = True
                break
            else:
                try:
                    userlist = [ p['name'] for p in data]
                except:
                    userlist = []
                if not name:
                    print("用户名为空，请重新输入")
                elif name in userlist:
                    print("改用户已存在，请重新输入")
                else:
                    break
        if flag:
            print("注册中断，退回主页面")
            break
        while True:
            passwd = getpass.getpass("""请输入你的密码,至少三位""")
            if passwd == "q" or passwd == "Q":
                print("退出！！！回到主页面")
                flag = True
                break
            else:
                if len(passwd) <= 2:
                    print("输入密码位数不正确，请重新输入")
                else:
                    break
        if flag:
            print("注册中断，退回主页面")
            break
        h = hashlib.md5()
        h.update(passwd.encode(encoding='utf-8'))
        passwd = h.hexdigest()
        while True:
            qq = input("请输入你的新qq号，需要是8-10位的整数:")
            if qq == "q" or qq == "Q":
                print("退出！！！回到主页面")
                flag = True
                break
            elif not qq:
                print("qq号不允许为空字符，请重新输入")
                continue
            else:
                try:
                    qq = int(qq)
                except:
                    print("你的qq号不是整数，请重新输入")
                    continue
                else:
                    if len(str(qq)) in range(8, 12):
                        break
                    else:
                        print("输入qq号码位数不对，请重新输入qq号")

        if flag:
            print("注册中断")
            break
        while True:
            server = input("请输入你的服务区，不允许为空:")
            if server == "q" or qq == "Q":
                print("""退出！！！回到主页面
                          注册失败！！！！
                    """)
                break
            else:
                if server:
                    print("""
                        注册成功！！！
                        您的用户名为：{}
                        你的qq号为：{}
                        你的服务区为：{}
                        """.format(name, qq, server))
                    failed_time = 0
                    login_time = time.time()
                    data.append({"name":name, "password":passwd, "qq":qq, "server":server,"failed_time":failed_time,"login_time":login_time})
                    data_json = json.dumps(data)
                    with open("mysql.txt","w") as f:
                        f.write(data_json)
                        # line = name + '\t' + passwd + '\t' + str(qq) + '\t' + server + '\n'
                        # f.write(line)
                    break
                else:
                    print("你的服务区输入有误，请重新输入")
        break
#删除用户
def delete():
    with open("mysql.txt", "r+") as f:
        file = f.read()
        data = json.loads(file)
    print("""
    删除用户相关信息，谨慎操作！！！！
    按q & Q取消操作：
    """)
    while True:
        name = input("""删除你所指定的用户:""").strip()
        if not name:
            print("你输入的为空，请重新输入")
        else:
            try:
                userlist = [p['name'] for p in data]
            except:
                userlist = []
            if name in userlist:
                po = userlist.index(name)
                data.pop(po)
                data = json.dumps(data)
                with open("mysql.txt", "w") as f:
                    f.write(data)
                print("删除用户{}成功！！！".format(name))
                break
            else:
                print("你所输入的用户不存在，请重新输入")
#修改用户
def change():
    print("""
    改用户信息
    q & q)退出修改页面
    """)
    with open("mysql.txt", "r+") as f:
        file = f.read()
        data = json.loads(file)
    while True:
        flag = False
        while True:
            name = input(""" 输入你要修改的用户名,不允许为空:""").strip()
            if name == "q" or name == "Q":
                flag = True
                break
            else:
                userlist = [p['name'] for p in data]
                if not name:
                    print("用户名不能为空，请重新输入")
                elif name not in userlist:
                    print("该用户不存在，请重新输入")
                else:
                    break
        if flag:
            print("取消修改，退回主页面")
            break
        while True:
            passwd = getpass.getpass("""请输入你的密码,至少三位""")
            if passwd == "q" or passwd == "Q":
                flag = True
                break
            else:
                if len(passwd) <= 2:
                    print("输入密码位数不正确，请重新输入")
                else:
                    break
        if flag:
            print("修改中断，退回主页面")
            break
        h = hashlib.md5()
        h.update(passwd.encode(encoding='utf-8'))
        passwd = h.hexdigest()
        while True:
            qq = input("请输入你的新qq号，需要是8-10位的整数:").strip()
            if qq == "q" or qq == "Q":
                flag = True
                break
            elif not qq:
                print("qq号不允许为空字符，请重新输入")
                continue
            else:
                try:
                    qq = int(qq)
                except:
                    print("你的qq号不是整数，请重新输入")
                    continue
                else:
                    if len(str(qq)) in range(8, 12):
                        break
                    elif int(str(qq)[0]) == 0:
                        print("不允许qq用0开头")
                    else:
                        print("输入qq号码位数不对，请重新输入qq号")

        if flag:
            print("修改中断")
            break
        while True:
            server = input("请输入你的服务区，不允许为空:").strip()
            if server == "q" or qq == "Q":
                print("""退出！！！回到主页面
                               修改失败！！！！
                         """)
                break
            else:
                if server:
                    print("""
                             修改成功！！！
                             您的用户名为：{}
                             你的qq号为：{}
                             你的服务区为：{}
                             """.format(name, qq, server))
                    userlist = [p['name'] for p in data]
                    po = userlist.index(name)
                    data[po]["passwd"] = passwd
                    data[po]["name"] = name
                    data[po]["qq"] = qq
                    data[po]["server"] = server
                    data  = json.dumps(data)
                    with open("mysql.txt","w") as f:
                            f.write(data)
                    break
                else:
                    print("你的服务区输入有误，请重新输入")
        break
#展示用户
def show():
    print("""
    展示已经注册了账号，默认每页最多3个用户数据，按N翻到下一页，按P翻到上一页
        p & P)跳转到前一页
        n & N)跳转到下一页
        q & Q)退出分页，回到主界面   
        """)
    with open("mysql.txt", "r+") as f:
        file = f.read()
        data = json.loads(file)
    if len(data) % 3 == 0:
        maxpage = len(data) // 3
    else:
        maxpage = len(data) // 3 + 1
    page = 1
    print("当前页数为{}".format(page))
    print("用户名              qq号             服务区")
    if len(data) > 3:
        for i in range(0, 3):
            print("{}             {}            {}".format(data[i]["name"], data[i]["server"], data[i]["qq"]))
    else:
        for i in range(0, len(data)):
            print("{}             {}            {}".format(data[i]["name"], data[i]["server"], data[i]["qq"]))
    while True:
        print("当前页数为{}".format(page))
        choose = input(""" please input your choose:     
            :""").strip()
        if choose == "p" or choose == "P":
            if page == 1:
                print("无法跳转到前一页，本页已经是第一页了")
                if len(data) > 3:
                    for i in range(0, 3):
                        print("{}             {}            {}".format(data[i]["name"], data[i]["server"], data[i]["qq"]))
                else:
                    for i in range(0, len(data)):
                        print("{}             {}            {}".format(data[i]["name"], data[i]["server"], data[i]["qq"]))
            else:
                page = page - 1
                for i in range((page - 1) * 3, page * 3 ):
                    print("{}             {}            {}".format(data[i]["name"], data[i]["server"], data[i]["qq"]))
        elif choose == "N" or choose == "n":
            if page == maxpage:
                print("无法跳转到下一页，本页已经是最后一页了")
                for i in range(3 * (page - 1), len(data)):
                    print("{}             {}            {}".format(data[i]["name"], data[i]["server"], data[i]["qq"]))
            else:
                if page != maxpage - 1:
                    for i in range(page * 3, page * 3 + 3):
                        print("{}             {}            {}".format(data[i]["name"], data[i]["server"], data[i]["qq"]))
                else:
                    for i in range(page * 3, len(data)):
                        print("{}             {}            {}".format(data[i]["name"], data[i]["server"], data[i]["qq"]))
                page = page + 1
        elif choose == "q" or choose == "Q":
            print("取消分页，退出到主页面")
            break
        else:
            print("输入有误，请重新输入")
#查询用户
def find():
    print("""尊敬的用户，您好！！！欢迎使用查询功能
    请输入您的选择！！！
    q & Q)退出本页面   """)
    with open("mysql.txt", "r+") as f:
        file = f.read()
        data = json.loads(file)
    while True:
            name = input(""" 输入查询用户名称,不允许为空:""").strip()
            if name == "q" or name == "Q":
                break
            else:
                userlist = [p['name'] for p in data]
                if not name:
                    print("用户名为空，请重新输入")
                elif name not in userlist:
                    print("该用户不存在，请重新输入")
                else:
                    p = userlist.index(name)
                    print("""
                    查询用户成功！！！！
                    用户名 :  {}
                    qq号：    {}
                    server:   {}                    
                    """.format(name,data[p]["qq"],data[p]["server"]))
#登录
def login():
    print("""尊敬的用户，你好！！！欢迎来到青铜组LOL后台系统！！！
    请输入您的选择！！！
    q & Q)退出程序               
    """)
    with open("mysql.txt", "r+") as f:
        file = f.read()
        data = json.loads(file)
    while True:
        flag = False
        while True:
            name = input(""" 输入你的用户名,不允许为空:""").strip()
            if name == "q" or name == "Q":
                flag = True
                break
            else:
                userlist = [p['name'] for p in data]
                if not name:
                    print("用户名为空，请重新输入")
                elif name not in userlist:
                    print("该用户不存在，请重新输入")
                else:
                    po = userlist.index(name)
                    if time.time() - data[po]['login_time'] > 86400:
                        data[po]['failed_time'] = 0
                        data[po]['login_time'] = time.time()
                    if data[po]['failed_time'] >= 3:
                        print("本日三次机会已经用完，请24小时之后再次登陆")
                        flag = True
                    break
        if flag:
            print("登录取消，退回主页面")
            break
        while True:
            passwd = getpass.getpass("""请输入你的密码,至少三位""")
            if passwd == "q" or passwd == "Q":
                print("退出！！！回到主页面")
                flag = True
                break
            else:
                if len(passwd) <= 2:
                    print("输入密码位数不正确，请重新输入")
                else:
                    h = hashlib.md5()
                    h.update(passwd.encode(encoding='utf-8'))
                    passwd = h.hexdigest()
                    if data[po]['password'] == passwd:
                        print("""
                        welcome！！！！{}先生/女士
                            恭喜您！！！登录成功！！！
                        你可以自由的操作后台数据
                        """.format(name))
                        failed_time = 0
                        operation()
                        break
                    else:
                        print("用户名密码不匹配，登陆失败！！！,退出程序")
                        data[po]['failed_time'] += 1
                        data = json.dumps(data)
                        with open("mysql.txt", "w") as f:
                            f.write(data)
                        break
        break
#操作流程
def operation():
    print("""
        尊敬的用户，你好！！！欢迎来到青铜组后台，本着对我大LOL的热爱，希望你能开心，
        emmmmmmmmmm,修改、查看、删除等骚操作也是可以的！！！why you are so 屌 ，
        不说了，开打开打
            """)
    while True:
        request = input("""
        请输入您的选择！！！（友情提示：不按套路出牌肯定不好使，q或者Q也行）
            d&D)删除某个小婊砸的信息
            c&C)修改用户信息
            f&F)查询用户信息
            s&S)查看所有列表（俺们支持分页)
            q&Q)退出后台        
        :""").strip()
        if request == 'd' or request == 'D':
            delete()
        if request == 'f' or request == 'F':
            find()
        elif request == 'c' or request == 'C':
            change()
        elif request == 's' or request == 'S':
            show()
        elif request == 'q' or request == 'Q':
            print("""后台退散 """)
            break
        else:
            print("请按照套路出牌")
######################################################################################################################################################3
####主程序###################################
print("""
          尊敬的用户您好！！！！欢迎来到青铜组的欢乐时刻！！！
    希望您使用愉快！！！！！！！！！！！
    """)
while True:
    choose = input("""
       q & Q)退出程序
       a & A)注册新的用户
       l & L)登录至后台系统
    :""").strip()
    if choose == 'a' or choose == 'A':
        add()
    elif choose == 'l' or choose == 'L':
        login()
    elif choose == 'q' or choose == 'Q':
        print("""sa   yo   na   la """)
        break
    else:
        print("请按照套路出牌")