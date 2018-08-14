#encoding: utf-8
from getpass import getpass

logininfo = ('admin', '51reboot')
login_num = 0

#打印输出格式控制
tpl_titile = '|{0:^9s}|{1:^11s}|{2:^7s}|{3:^15s}|{4:^11s}|'
colums_titile = ('ID','NAME','AGE','TEL','ADDRESS')
titile = tpl_titile.format(colums_titile[0], colums_titile[1], colums_titile[2], colums_titile[3], colums_titile[4])
split_titile = '-' * (len(titile))
tpl_users = '|{0:^9s}|{1:^11s}|{2:^7s}|{3:^15s}|{4:^11s}|'

#系统登录
while True:
    if login_num >= 3:
        break
    else:
        username = input('please input user name:')
        password = getpass('please input password:')
        if username == logininfo[0] and password == logininfo[1]:
            print('\033[32mwelcome sign in mgt!\n\033[0m')

            #读取用户列表,用户列表文件在脚本同一目录下如果没有则系统新建userdata.txt存储数据
            userlist = []
            with open('userdata.txt', 'a+t') as fhandler:
                fhandler.seek(0)
                userlist_txt = fhandler.read().split('\n')
                if userlist_txt[0] != '':
                    for x in userlist_txt:
                        userdata = x.split(',')
                        if userdata[0] != '':
                            userlist.append(userdata)

            #进入系统主菜单
            while True:
                op = input('Please input action(list/add/update/delete/find/exit):')
                op = op.strip()

                if op == 'list':
                    '''
                    ---------------------------------------------
                    | id |   name   | age |   tel     |  address |
                    ---------------------------------------------
                      1    monkey     28   132xxxxxxxx   beijing
                      2   zhengyscn   21   135xxxxxxxx   shanghai
                      3      wd       28   131xxxxxxxx   zhengzhou
                      4    xuegao     28   139xxxxxxxx   shandong
                    ---------------------------------------------
                    '''
                    #分页显示，每5条记录1页,U翻上页，D翻下页，Q退出
                    page_count = ((len(userlist)-1) // 5) + 1
                    page_num = 0
                    page_end = 0
                    row_num = 0

                    while True:
                        if page_end == 0:
                            print('{0}\n{1}\n{2}'.format(split_titile, titile, split_titile))
                            for i in userlist[row_num : row_num + 5]:
                                print(tpl_users.format(str(i[0]), i[1], i[2], i[3], i[4]))
                            page_info = 'page ' + str(page_num + 1) + ' of ' + str(page_count)
                            print('{0}\n{1:^53}'.format(split_titile, page_info))
                            while True:
                                page_op = input('Input U to the previous page, D to the next page, Q exit:')
                                if page_op.upper() == 'U':
                                    if (page_num + 1) == 1:
                                        print('This page is the first page!')
                                    else:
                                        page_num -= 1
                                        row_num -= 5
                                        break
                                elif page_op.upper() == 'D':
                                    if (page_num + 1) == page_count:
                                        print('This page is the last page!')
                                    else:
                                        page_num += 1
                                        row_num += 5
                                        break
                                elif page_op.upper() == 'Q':
                                    page_end = 1
                                    break
                                else:
                                    print("\033[31mInvalid cmd.\033[0m")
                        else:
                            break


                elif op == 'add':
                    '''
                        新增用户录入信息：monkey/28/132xxx/beijing
                    '''
                    useradd = input('Please input userdata(name/age/tel/address):')
                    userdata = useradd.split('/')

                    if len(userdata) == 4 and userdata[3] != '':
                        if len(userlist) == 0:
                            uid = str(1)
                        else:
                            uid = str(max([int(i[0]) for i in userlist]) + 1)

                        userdata.insert(0, uid)
                        userlist.append(userdata)
                        #打印添加的用户信息
                        print('\033[32mAdd user success!~\033[0m')
                        print('{0}\n{1}\n{2}\n{3}\n{4}'.format(split_titile, titile, split_titile,
                                                               tpl_users.format(str(userdata[0]), userdata[1],
                                                                                userdata[2], userdata[3], userdata[4]),
                                                               split_titile))
                        #存储用户信息到文件
                        with open('userdata.txt', 'wt') as fhandler:
                            for x in userlist:
                                fhandler.write('{},{},{},{},{}\n'.format(str(x[0]), x[1], x[2], x[3], x[4]))
                    else:
                        print('\033[31mInput format error!Please re-enter.\033[0m')


                elif op == 'update':
                    '''
                        更改用户信息输入格式：monkey/28/132xxx/beijing
                    '''
                    uid = input('Please input user ID:')

                    if uid not in [i[0] for i in userlist]:
                        print('\033[31mUser does not exist!~\033[0m')
                    else:
                        userupdate = input('Please input userdata(name/age/tel/address):')
                        userdata = userupdate.split('/')
                        if len(userdata) == 4 and userdata[3] != '':
                            for i in userlist:
                                if uid == i[0]:
                                    i[1],i[2],i[3],i[4] = userdata[0],userdata[1],userdata[2],userdata[3]
                                    # 打印修改的用户信息
                                    print('\033[32mUpdate user data success!~\033[0m')
                                    print('{0}\n{1}\n{2}\n{3}\n{4}'.format(split_titile, titile, split_titile,
                                                                           tpl_users.format(str(i[0]), i[1], i[2], i[3],
                                                                                            i[4]), split_titile))
                                    # 存储用户信息到文件
                                    with open('userdata.txt', 'wt') as fhandler:
                                        for x in userlist:
                                            fhandler.write('{},{},{},{},{}\n'.format(str(x[0]), x[1], x[2], x[3], x[4]))
                        else:
                            print('\033[31mInput format error!Please re-enter.\033[0m')


                elif op == 'delete':
                    '''
                        按用户ID删除用户：delete 1
                    '''
                    uid = input('Please input user ID:')
                    if uid not in [i[0] for i in userlist]:
                        print('\033[31mUser does not exist!~\033[0m')
                    else:
                        for i in userlist:
                            if uid == i[0]:
                                del userlist[userlist.index(i)]
                                print('\033[32mDelete user success!~\033[0m')
                                # 存储用户信息到文件
                                with open('userdata.txt', 'wt') as fhandler:
                                    for x in userlist:
                                        fhandler.write('{},{},{},{},{}\n'.format(str(x[0]), x[1], x[2], x[3], x[4]))


                elif op == 'find':
                    '''
                        按用户ID查找用户：find 1
                        按用户名字查找用户：find monkey
                    '''
                    user = input('Please input user name or user ID:')
                    user = user.strip()
                    if ((user not in [i[1] for i in userlist]) and (user not in [i[0] for i in userlist])):
                        print('\033[31mUser does not exist!~\033[0m')
                    else:
                        for i in userlist:
                            if user == i[1] or user == i[0]:
                                print('{0}\n{1}\n{2}\n{3}\n{4}'.format(split_titile, titile, split_titile,
                                                                       tpl_users.format(str(i[0]), i[1], i[2], i[3],
                                                                                        i[4]), split_titile))


                elif op == 'exit':
                    break


                else:
                    print("\033[31mInvalid cmd.\033[0m")   # 加上颜色 警告信息
        else:
            print('\033[31musername or password error!\nPlease login again!\033[0m')
            login_num += 1


print("\033[36mLogout!Welcome to login next time.\033[0m")
