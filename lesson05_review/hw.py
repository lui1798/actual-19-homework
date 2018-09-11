
'''
    登录认证
'''

# USERPASS = ('51reboot', '123654')
# CNT = 1
#
#
# # 0. while循环
# while CNT <=3 :
#
#     # 1. 先输入用户名和密码
#     username = input("please input your username: ")
#     password = input("please input your password: ")
#
#     # 2. 判断用户名和密码是否正确
#     if username == USERPASS[0] and password == USERPASS[1]:
#
#     # 3. 验证成功，打印登录成功的信息；验证失败， 重试3次；
#         print("Username {} login sucess.".format(username))
#     # 4. 3次登录失败 锁定一天
#     else:
#         print("Username {} login failed, Please try continue, failed count {}".format(username, CNT))
#         CNT += 1
#
#     # 5. 解锁

# USERPASS = ('51reboot', '123654')
# INIT_CNT = 5
# MAX_CNT = 5
#
# # 0. while循环
# while INIT_CNT <= MAX_CNT and INIT_CNT >0:
#
#     # 1. 先输入用户名和密码
#     username = input("please input your username: ")
#     password = input("please input your password: ")
#
#     # 2. 判断用户名和密码是否正确
#     if username == USERPASS[0] and password == USERPASS[1]:
#
#     # 3. 验证成功，打印登录成功的信息；验证失败， 重试3次；
#         print("Username {} login sucess.".format(username))
#     # 4. 3次登录失败 锁定一天
#     else:
#         print("Username {} login failed, Please try continue, you have {} time.".format(username, INIT_CNT-1))
#         INIT_CNT -= 1
#
#     # 5. 解锁


# USERPASS = ('51reboot', '123654')
# CNT = 5
#
#
# # 0. while循环
# while CNT <= 5 and CNT > 0:
#
#     # 1. 先输入用户名和密码
#     username = input("please input your username: ")
#     password = input("please input your password: ")
#
#     # 2. 判断用户名和密码是否正确
#     if username == USERPASS[0] and password == USERPASS[1]:
#
#     # 3. 验证成功，打印登录成功的信息；验证失败， 重试3次；
#         print("Username {} login sucess.".format(username))
#     # 4. 3次登录失败 锁定一天
#     else:
#         print("Username {} login failed, Please try continue, you have {} time.".format(username, CNT-1))
#         CNT -= 1
#
#     # 5. 解锁


'''
    对用户信息进行修改
    name monkey1
        age 20
        tel 182xxx
'''

USERINFO = [
    {'id' : 1, 'name' : 'monkey1', 'age' : 18, 'tel' : '132xxx', 'address' : 'beijing'},
    {'id' : 2, 'name' : 'monkey2', 'age' : 19, 'tel' : '152xxx', 'address' : 'beijing'}
]

# 1. 接受用户输入的id
uid = input("please input your uid: ")

for obj in USERINFO:
# 2. 判断id是否存在
    if int(uid) == obj.get('id'):
# 2.1 存在 这一行用户信息
#         print(obj)

# 2.1.1 提示输入信息
# 2.1.2 更新信息， 提示ok
#         obj['age'] = 20
#         obj['tel'] = '182xxx'
#         USERINFO[obj]['age'] = 20
        idx = USERINFO.index(obj)
        USERINFO[idx].update({'age' : 20, 'tel' : '182xxx'})
        break
# 2.2 输入不存在信息
    else:
        print("uid not found.")

print(USERINFO)