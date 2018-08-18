
# 用户管理系统
# 1.登录认证
# 2.增删改查
# 3.格式华输出
# userinfo格式[1, 'monkey2', 20, '132xxx', 'beijing']
# －－－－－－－－－－－－－－－－－－－－－－－－－－－－

# 用到的变量
  # newuser 添加用户时的新用户 字符串
  #newuser_list 把newuser的转为列表
  #userinfo用户信息表
  #uid用户信息表中的编号 也就userinfo这个列的第一位
  #NewId  用户信息表的新编号  每次添加用户时递增

# ---------------------------------------------------------


#定义一个空列表userinfo
userinfo = []
#设置登录账号和密码
loginUser = ('admin', '123')
#设定一个计数器（登录时输错3次密码就不上输入了）
count = 3


while True:
    username = input("输入用户名: ")
    password = input("输入登录密码: ")
    # 如果username等于正确的用户名和密码
    if username == loginUser[0] and password == loginUser[1]:
        op = input("请输入操作 add delete update list: ")
        if op == 'add':
            newuser = input("输入用户信息以空格分隔: ")        #提示输入新用户信息
            newuser_list = newuser.split(' ')     # 把字符串转成列表  例如 L＝"aa bb cc" 然后执行 L.split(' ')就会以空格为分隔生成列表['aa','bb','cc']
            if len(userinfo) == 0:                #如果用户信息等于空   len统计列表元素的个数 例如 L=[8,8,8]  len(L)的结果为3
                newuser_list.insert(0, 1)         #在新用户0的位置插入1 ,也就是插入编号1
                userinfo.append(newuser_list)     #把新输入的用户插入userinfo
            else:
                uid=[x[0] for x in userinfo]      #遍历userinfo 取出第1位（编号）定义为uid
                NewId=max(uid)+1                  #从上边的遍历结果中找出最大值 加1  定义为NewId
                newuser_list.append(0,NewId)      #把新输入的用户加上编号
                userinfo.append(newuser_list)

# ______________________________________________________________________________________________________________________________________________________

        elif op == 'delete':                    #如果用户执行删除操作
            print(userinfo)
            uid = input("输入要删除的用户编号: ")
            for x in userinfo:
                if x[0] == int(uid):
                    userinfo.remove(x)
# ______________________________________________________________________________________________________________________________________________________
        elif op == 'update':                   #如果用户执行更新操作
            print(userinfo)
            uid = input("请输入要更新的用户编号：")
            for x in userinfo:
                if x[0] ==int(uid)
                    userinfo[uid]=

        elif op == 'list':
            pass
        elif op == 'find':
            '''
            find 1
            find monkey2
            '''
        elif op == 'exit':
            print("-------退出信息-----------")
            break
        else:
            print("invalid op.")
    else:
    #     print("login failed.")