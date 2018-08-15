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
userlist = []  ##userlist:存放系统数据
s = ''  ##用于临时存储从userlist.txt读取的每一行数据
###读取userlist.txt中的用户信息，存储到userlist中###
with open("./userlist.txt", "r") as f:
    while True:
        s = f.readline()
        if s == "":
            break
        userlist.append(s.strip())

###用户操作###
while True:
    print("\033[34m\"list\" (:to list all user) \033[0m")
    print("\033[34m\"add\" (:to add user)\033[0m ")
    print("\033[34m\"update\" (:to update user information)\033[0m")
    print("\033[34m\"delete\" (:to delete user information)\033[0m")
    print("\033[34m\"find\" (:to find certain user information)\033[0m")
    print("\033[34m\"exit\" (:to quit)\033[0m")
    op = input('\033[34m please input action: \033[0m')
    if op == 'list':
        print("--------------------------------------")
        print(" id\t    name\t   age\t tel\t address\t")
        for u in userlist:
            print(u.replace(" ", "\t"))
        print("--------------------------------------")
    elif op == 'add':
        max_index = 0
        for x in userlist:

            if max_index < int(x[0:4]):
                max_index = int(x[0:4])
        print("user information --->name\t age\t tel\t address\t")
        user_in = input("please input user information:")
        userlist.append(str(max_index + 1).zfill(4) + " " + user_in)
        # zfill来调整格式，如果是2，则前面自动补成0002
        print("--user information add successfully!!!--")

    elif op == 'update':
        '''
            monkey 28 132xxx beijing
        '''
        user_id = input("--please input an id to update(id must be XXXX):")
        print("user information --->name\t age\t tel\t address\t")
        user_new = input("please input user information:")
        # 先获取此id对应的index，然后对此index 重新赋值
        for x in userlist:
            if x[0:4] == user_id:
                index = userlist.index(x)
                userlist[index] = user_id + " " + user_new

    elif op == 'delete':
        '''
            delete 1
        '''
        user_id = input("--please input an id to update(id must be XXXX):")
        for x in userlist:
            if x[0:4] == user_id:
                index = userlist.index(x)
                user_del = userlist.pop(index)
        print("{} delete successfully!!".format(user_del))

    elif op == 'find':
        '''
            find 1
            find monkey
        '''
        user_info = input("please input user id or name:")
        for x in userlist:
            if x.find(user_info) != -1:
                print("user information: {}".format(x))

    elif op == 'exit':
        break

    else:
        print("\033[31m invalid cmd!!!\033[0m")  # 加上颜色 警告信息

print("\033[32m Login out\033[0m")
print("\033[32m ------------------------------------\033[0m")

###将userlist写入到txt文件中###
with open("./userlist.txt", "w+") as f:
    for x in userlist:
        f.write(x)
        f.write("\n")
    f.close()
