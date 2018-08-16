#!/usr/bin/env python3
import  getpass
import hashlib
#添加用户
def add():
    print("""欢迎注册（请输入用户名、密码、qq号、所在服务区）
        eg:   zhangsan   123   123  艾欧尼亚    
        """)
    while True:
        flag = False
        while True:
            name = input(""" 输入你的用户名,不允许为空:""")
            if name == "q" or name == "Q":
                print("退出！！！回到主页面")
                flag = True
                break
            else:
                userlist = [x[0] for x in data]
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
                    data.append([name, passwd, qq, server])
                    with open("mysql.txt","a+") as f:
                        line = name + '\t' + passwd + '\t' + str(qq) + '\t' + server + '\n'
                        f.write(line)
                    break
                else:
                    print("你的服务区输入有误，请重新输入")
        break
#删除用户
def delete():
    print("""
    删除用户相关信息，谨慎操作！！！！
    按q & Q取消操作：
    """)
    while True:
        name = input("""删除你所指定的用户:""")
        if not name:
            print("你输入的为空，请重新输入")
        else:
            userlist = [x[0] for x in data]
            if name in userlist:
                p = userlist.index(name)
                data.pop(p)
                with open("mysql.txt", "w") as f:
                    for i in range(0, len(data)):
                        name = data[i][0]
                        passwd = data[i][1]
                        qq = data[i][2]
                        server = data[i][3]
                        line = name + '\t' + passwd + '\t' + str(qq) + '\t' + server + '\n'
                        f.write(line)
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
    while True:
        flag = False
        while True:
            name = input(""" 输入你要修改的用户名,不允许为空:""")
            if name == "q" or name == "Q":
                flag = True
                break
            else:
                userlist = [x[0] for x in data]
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
            qq = input("请输入你的新qq号，需要是8-10位的整数:")
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
            server = input("请输入你的服务区，不允许为空:")
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
                    userlist = [x[0] for x in data]
                    p = userlist.index(name)
                    data[p][1] = passwd
                    data[p][2] = qq
                    data[p][3] = server
                    with open("mysql.txt","w") as f:
                        for i in range(0,len(data)):
                            name   = data[i][0]
                            passwd = data[i][1]
                            qq     = data[i][2]
                            server = data[i][3]
                            line = name + '\t' + passwd + '\t' + str(qq) + '\t' + server + '\n'
                            f.write(line)
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
    maxpage = len(data) // 3 + 1
    page = 1
    print("当前页数为{}".format(page))
    print("用户名              qq号             服务区")
    if len(data) > 3:
        for i in range(0, 3):
            print("{}             {}            {}".format(data[i][0], data[i][2], data[i][3]))
    else:
        for i in range(0, len(data)):
            print("{}             {}            {}".format(data[i][0], data[i][2], data[i][3]))
    while True:
        print("当前页数为{}".format(page))
        choose = input(""" please input your choose:     
            :""")
        if choose == "p" or choose == "P":
            if page == 1:
                print("无法跳转到前一页，本页已经是第一页了")
                if len(data) > 3:
                    for i in range(0, 3):
                        print("{}             {}            {}".format(data[i][0], data[i][2], data[i][3]))
                else:
                    for i in range(0, len(data)):
                        print("{}             {}            {}".format(data[i][0], data[i][2], data[i][3]))
            else:
                page = page - 1
                for i in range((page - 1) * 3, page * 3 ):
                    print("{}             {}            {}".format(data[i][0], data[i][2], data[i][3]))
        elif choose == "N" or choose == "n":
            if page == maxpage:
                print("无法跳转到下一页，本页已经是最后一页了")
                for i in range(3 * (page - 1), len(data)):
                    print("{}             {}            {}".format(data[i][0], data[i][2], data[i][3]))
            else:
                if page != maxpage - 1:
                    for i in range(page * 3, page * 3 + 3):
                        print("{}             {}            {}".format(data[i][0], data[i][2], data[i][3]))
                else:
                    for i in range(page * 3, len(data)):
                        print("{}             {}            {}".format(data[i][0], data[i][2], data[i][3]))
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
    while True:
            name = input(""" 输入查询用户名称,不允许为空:""")
            if name == "q" or name == "Q":
                break
            else:
                userlist = [x[0] for x in data]
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
                    """.format(name,data[p][2],data[p][3]))
#登录
def login():
    print("""尊敬的用户，你好！！！欢迎来到青铜组LOL后台系统！！！
    请输入您的选择！！！
    q & Q)退出程序               
    """)
    while True:
        flag = False
        while True:
            name = input(""" 输入你的用户名,不允许为空:""")
            if name == "q" or name == "Q":
                flag = True
                break
            else:
                userlist = [x[0] for x in data]
                if not name:
                    print("用户名为空，请重新输入")
                elif name not in userlist:
                    print("该用户不存在，请重新输入")
                else:
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
                    userlist = [x[0] for x in data]
                    p = userlist.index(name)
                    if data[p][1] == passwd:
                        print("""
                        welcome！！！！{}先生/女士
                            恭喜您！！！登录成功！！！
                        你可以自由的操作后台数据
                        """.format(name))
                        operation()
                        break
                    else:
                        print("用户名密码不匹配，登陆失败！！！,退出程序")
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
        :""")
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
data = []
with open('mysql.txt', 'r+') as f:
    for line in f:
        line = line.replace("\n","")
        name = line.split("\t")[0]
        passwd = line.split("\t")[1]
        qq = int(line.split("\t")[2])
        server = line.split("\t")[3]
        data.append([name,passwd,qq,server])
print("""
          尊敬的用户您好！！！！欢迎来到青铜组的欢乐时刻！！！
    希望您使用愉快！！！！！！！！！！！
    """)
while True:
    choose = input("""
       q & Q)退出程序
       a & A)注册新的用户
       l & L)登录至后台系统
    :""")
    if choose == 'a' or choose == 'A':
        add()
    elif choose == 'l' or choose == 'L':
        login()
    elif choose == 'q' or choose == 'Q':
        print("""sa   yo   na   la """)
        break
    else:
        print("请按照套路出牌")