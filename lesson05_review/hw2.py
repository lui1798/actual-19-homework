

'''
    需求：
        合并 登录 和 修改 的代码
'''

USERPASS = ('admin', '123456')
CNT = 1
EXIT_FLAG = False

USERINFO = [
    {'id' : 1, 'name' : 'monkey1', 'age' : 18, 'tel' : '132xxx', 'address' : 'beijing'},
    {'id' : 2, 'name' : 'monkey2', 'age' : 19, 'tel' : '152xxx', 'address' : 'beijing'}
]


'''
    CNT <=3 and not EXIT_FLAG  ----> False
    True and False
    False and False
    False and True
'''


# 0. while循环
# while CNT <=3 and not EXIT_FLAG:
while CNT <=3:

    if EXIT_FLAG:
        break

    # 1. 先输入用户名和密码
    username = input("please input your username: ")
    password = input("please input your password: ")

    # 2. 判断用户名和密码是否正确
    if username == USERPASS[0] and password == USERPASS[1]:


        '''
            修改用户信息
        '''
        while 1:
            op = input("please input your oper: ")
            if op == 'update':
                print("----------------Before----------------------")
                print(USERINFO)
                uid = input("please input your uid: ")
                for obj in USERINFO:
                    if int(uid) == obj.get('id'):
                        idx = USERINFO.index(obj)
                        USERINFO[idx].update({'age': 20, 'tel': '182xxx'})
                        EXIT_FLAG = True
                        break
                else:
                    print("uid not found.")

            elif op == 'exit':
                EXIT_FLAG = True
                break
            else:
                print("invalid op.")

    # 3. 验证成功，打印登录成功的信息；验证失败， 重试3次；
    #     print("Username {} login sucess.".format(username))
    # 4. 3次登录失败 锁定一天
    else:
        print("Username {} login failed, Please try continue, failed count {}".format(username, CNT))
        CNT += 1


    # 5. 解锁

print("----------------After----------------------")
print(USERINFO)
