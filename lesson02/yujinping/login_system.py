# encoding = utf-8

# 空列表 用来存储user信息
userinfo = []
string = ''

# 读文件
with open('userinfo', 'r') as f:
    while True:
        # 按行读文件
        string = f.readline()
        if string == '':
            break
        # 放入列表中 去掉空格
        userinfo.append(string.strip())

while True:

    # 输入操作
    operation = input('Please input user operation: ')

    # 列出文件list
    if operation == 'list':
        print('-----------------------------------')
        print('id\t name\t age\t tel\t address\t')
        print('-----------------------------------')
        # 循环出所有user
        for user in userinfo:
            print(user)
        print('-----------------------------------')

    elif operation == 'add':

        user_num = 0
        # 获取最后一行数据的id
        for user in userinfo:
            if user_num < int(user[0]):
                user_num = int(user[0])
        user_info = input('Please input user information: ')
        # 添加新增行
        userinfo.append(str(user_num + 1) + ' ' + user_info)
        print('add success!')

    elif operation == 'update':
        # 输入要更新user的id
        user_id = input('Please input the id(x): ')
        # 输入要更新成的user信息
        user_info = input('Please input user message: ')
        # 循环列表，找出要更新的id
        for user in userinfo:
            if user[0] == user_id:
                # 赋值新的user信息，加上空格，留出id和name的空隙
                userinfo[userinfo.index(user)] = user_id + ' ' + user_info

    elif operation == 'delete':
        # 输入要删除的id
        user_id = input('Please input the id(x): ')
        # 循环，找到id
        for user in userinfo:
            if user[0] == user_id:
                # 删除user信息 str.pop([index])
                userinfo.pop(userinfo.index(user))

    elif operation == 'find':
        # 输入要查找的id或者name或者age等信息
        user_msg = input('Please input the id or user: ')
        # 循环查找
        for user in userinfo:
            # 如果在userinfo列表中查到信息（str.find()!=-1），打印user str.find(sub)
            if user.find(user_msg) != -1:
                print(user)

    elif operation == 'exit':
        break

    else:
        print('invalid cmd')

# 登出
print('Login out')

# 写文件
with open('userinfo', 'w') as f:
    # 循环列表 写入文件
    for x in userinfo:
        f.write(x)
        f.write('\n')
    # 关闭文件
    f.close()