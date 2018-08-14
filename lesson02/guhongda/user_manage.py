#encoding:utf-8

users = []
users.append((1,'tompson',29,123456))

tpl_title = '|{0:^10}|{1:^10}|{2:^5}|{3:^15}|'
tpl_format = tpl_title.format('ID','Name','Age','Tpl')
tpl_user = '|{0:^10}|{1:^10}|{2:^5}|{3:^15}|'
xin = '-' * len(tpl_format)
count = 2


for i in range(3):
    user_name = input('请输入用户名/密码，格式(usesname/password)：')
    username_list, passwd_list = user_name.split('/')
    passwd_list = int(passwd_list)
    user_exist = False
    for user_tuple in users:
        if user_tuple[1] == username_list and user_tuple[3] == passwd_list:
            user_exist = True
            break

    if user_exist:
        is_exits = True
        print('\033[32m认证成功！\033[0m')
        break
    else:
        is_exits = False
        print('\033[31m用户名或手机号码有误！还可输入{0}次\033[0m'.format(count))
        count -= 1

if is_exits:
    while True:
        status = input('请输入find/list/add/delete/update/exit:')
        if status == 'list':
            print(xin)
            print(tpl_format)
            print(xin)
            for user in users:
                print(tpl_user.format(user[0], user[1], user[2], user[3]))
            print(xin)
        elif status == 'add':
            max_count = 0
            for user in users:
                if user[0] > max_count:
                    max_count = user[0]
            user_name = input('请输入(Name,Age,Tpl)')
            user_exist = False
            for user in users:
                if user[1] == user_name.split(',')[0]:
                    print('用户名已存在,请输入其它用户名')
                    user_exist = True
                    break
            if not user_exist:
                max_count += 1
                user_list = user_name.split(',')
                user_tuple = (max_count,) + tuple(user_list)
                users.append(user_tuple)
        elif status == 'delete':
            user_name = input('请输入用户名：')
            user_exist = False
            for user in users:
                if user[1] == user_name.split(',')[0]:
                    user_exist = True
                    user_temp =  user
                    break
            if user_exist:
                users.remove(user_temp)
                print('{0}用户删除成功'.format(user_temp))
            else:
                print('用户不存在，请重新输入')

        elif status == 'update':
            user_name = input('请输入用户名：')
            user_exist = False
            for user in users:
                if user[1] == user_name.split(',')[0]:
                    user_exist = True
                    user_temp =  user
                    code = user[0]
                    break
            if user_exist:
                users.remove(user_temp)
                user_name = input('请输入(Name,Age,Tpl)')
                user_tuple = tuple(user_name.split(','))
                code = int(code)
                user_edit = (code,) + user_tuple
                users.append(user_edit)
            else:
                print('用户不存在，请重新输入')
        elif status == 'find':
            user_name = input('请输入查找的用户名：')
            user_exist = False
            for user in users:
                if user[1] == user_name:
                    user_exist = True
                    user_temp =  user
                    break
            if user_exist:
                print(tpl_user.format(user_temp[0],user_temp[1],user_temp[2],user_temp[3]))
            else:
                print('用户不存在，请重新输入')

        elif status == 'exit':
            break
