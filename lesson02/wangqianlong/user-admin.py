# #
# 作业：用户管理系统
#
# 1.登录认证
# 2.增删改查和搜索
#     2.1 增 add
#     2.2 删 delete
#     2.3 改 update
#     2.4 查 list
#     2.5 搜索 find
# 3.格式化输出


'''
查询和搜索到的用户信息列表呈现形式：

用户ID   姓名    年龄    电话       地址
  1     wang    28     131***    beijing
  2     hao     23     132***    shanghai
  3     pang    23     131***    beijing  
  4     ma      27     133***    beijing      

'''
#
import time

userinfo = [[1, 'wang', '27', '131****', 'beijing']]     #存储用户信息列表
logininfo = ('admin', '51reboot')

#登录成功界面
login_sucess = '''\033[32m
-----------------------------------
登录成功！本用户管理系统可以执行以下操作：
    1. 添加用户(add)
    2. 删除用户(delete)
    3. 更新用户(update)
    4. 查询用户(list)
    5. 按关键字搜索用户(find)
    6. 退出登录（exit）
-----------------------------------
\033[0m'''

logincount = 0    # count  次数限制3次，3次登录失败，2分钟后再登

BOOLEAN = True   # 设置退出程序的标记位
while BOOLEAN:
    username = input('\033[0;34m请输入用户名:\033[0m')
    password = input('\033[0;34m请输入密码:\033[0m')
    if username == logininfo[0] and password == logininfo[1]:
        # print('\033[0;32;40m登录成功!\033[0m')
        print(login_sucess)
        BOOL = True
        while BOOL:
            op = input('\033[0;34m请输入操作方式(add/delete/update/list/find/exit) :\033[0m')
            if op == 'add':
                # 实现：根据特定格式输入用户信息执行添加操作: name age tel address
                # 1.if 输入的用户信息列表中不存在，给新用户添加用户ID，增加到用户列表中；
                # 2.if 输入的用户信息列表中已存在，提示用户已存在。

                userinfo_input = input('\033[0;34m请输入用户信息(格式name age tel address):\033[0m')
                userinfo_list = userinfo_input.split(' ')
                if len(userinfo_list) == 4:

                    if len(userinfo) == 0:
                        userinfo_list.insert(0, 1)
                        userinfo.append(userinfo_list)
                        print('\033[0;33m添加成功，可以通过list查看！\033[0m')
                    else:
                        BOOL0 = False
                        for x in userinfo:
                            i = 0
                            while i < len(userinfo_list):
                                if userinfo_list[i] in x:
                                    i = i + 1
                                    BOOL0 = True
                                else:
                                    BOOL0 = False
                                    break
                        if  BOOL0 == False:
                            uids = [x[0] for x in userinfo]
                            new_id = max(uids) + 1
                            userinfo_list.insert(0, new_id)
                            userinfo.append(userinfo_list)
                            print('\033[0;33m添加成功，可以通过list查看！\033[0m')
                        else:
                            print('\033[0;33m用户已存在，请重新添加！\033[0m')

                else:
                    print('\033[0;31m未按格式要求输入!\033[0m')

                #print(userinfo)

            elif op == 'delete':
                # pass
                # 实现：按用户ID删除整个用户信息，且用户ID一旦建立不可更改，标识唯一用户；
                # 1.if 用户列表为空，不能执行删除操作；
                # 2.if 用户列表不为空，根据输入用户ID执行删除整个用户信息；
                # 3.if 用户ID存在，执行删除；
                # 4.if 用户ID不存在，提示请尝试通过搜索找到用户ID再尝试删除。

                if len(userinfo) != 0:
                    uid = int(input('\033[0;34m请输入用户ID:\033[0m'))
                    # max_uid =max([x[0] for x in userinfo])
                    if uid in [x[0] for x in userinfo]:
                        for x in userinfo:
                            if x[0] == uid:
                                userinfo.remove(x)
                            # elif x[0] > uid:
                            #     x[0]= x[0]-1
                    else:
                        print('\033[0;33m用户ID不存在，请通过搜索找到用户ID再尝试删除！\033[0m')
                else:
                    print('\033[0;31m用户信息列表为空，不能删除!\033[0m')
                print(userinfo)

            elif op == 'update':
                # pass
                '''
                 实现：根据用户ID修改用户年龄或电话或地址信息
                 1、if 用户列表为空，无需修改。
                 2、if 用户列表不为空，根据用户ID进行修改；
                 3、if 用户ID不存在，提示：请尝试通过搜索找到用户ID再进行修改；
                 4、if 用户ID存在，根据输入的age、tel、addr进行修改。
                '''
                if len(userinfo) != 0:
                    uidd = int(input('\033[0;34m请输入用户ID：\033[0m'))
                    # max_uid =max([x[0] for x in userinfo])
                    if uidd in [x[0] for x in userinfo]:
                        updateinfo = input('\033[0;34m请输入要修改的信息(age/tel/addr):\033[0m')

                        if updateinfo == 'age':
                            # pass
                            updateinfo_after = input('\033[0;34m请输入修改后年龄:\033[0m')
                            for x in userinfo:
                                if x[0] == uidd:
                                    x[2] = updateinfo_after
                            print('\033[0;33m修改成功，可以通过list查看！\033[0m')
                        elif updateinfo == 'tel':
                            # pass
                            updateinfo_after = input('\033[0;34m请输入修改后电话:\033[0m')
                            for x in userinfo:
                                if x[0] == uidd:
                                    x[3] = updateinfo_after
                            print('\033[0;33m修改成功，可以通过list查看！\033[0m')
                        elif updateinfo == 'addr':
                            # pass
                            updateinfo_after = input('\033[0;34m请输入修改后地址:\033[0m')
                            for x in userinfo:
                                if x[0] == uidd:
                                    x[4] = updateinfo_after
                            print('\033[0;33m修改成功，可以通过list查看！\033[0m')
                        else:
                            print('\033[0;31m无效输入，请检查是否输入的age/tel/addr!\033[0m')

                    else:
                        print('\033[0;33m用户ID不存在，请尝试通过搜索找到用户ID再进行修改！\033[0m')
                else:
                    print('\033[0;31m用户信息列表为空，无需修改，请尝试添加用户!\033[0m')


            elif op == 'list':
                #pass
                '''
                实现：显示当前用户信息列表中存在的所有用户；
                1.if 不存在用户，提示当前用户列表为空；
                2.if 存在用户列表，按格式显示出用户信息。
                
                '''
                if len(userinfo) == 0:
                    print('\033[0;31m当前用户列表信息为空！\033[0m')
                else:
                    print(' 用户ID    姓名    年龄      电话     地址')
                    for x in userinfo:
                        print('\033[0;32m{0:^5d}{1:>10s}{2:^10s}{3:^10s}{4:^10s}\033[0m'.format(x[0], x[1], x[2], x[3], x[4]))

            elif op == 'find':
                # pass
                '''
                实现：通过输入搜索关键字实现搜索功能；
                1、定义findsome 空列表，为了存储找到的匹配项信息；
                2、限制输入的关键字信息不大于5个；
                3、输入的关键字信息和用户信息列表的每一个用户信息进行对比；
                4、完全匹配，即为搜索成功，返回整个用户信息；否则返回未找到匹配项。
                '''
                findsome = []
                keywordinfo = input('\033[0;34m请输入搜索关键字（不大于5个，空格隔开）：\033[0m')
                keyword_list = keywordinfo.split(' ')
                for x in userinfo:
                    i = 0
                    BOOL2 = True
                    while i < len(keyword_list):
                        if keyword_list[i] in x:
                            BOOL2 = True
                            i = i + 1
                        else:
                            BOOL2 = False
                            break
                    if BOOL2:
                        findsome.append(x)
                if len(findsome) == 0:
                    print('\033[0;31m未找到匹配项!\033[0m')
                else:
                    print('\033[0;32m搜索的匹配项为:\033[0m')
                    for x in findsome:
                        print('\033[0;32m{0:^5d}{1:>10s}{2:^10s}{3:^10s}{4:^10s}\033[0m'.format(x[0], x[1], x[2], x[3], x[4]))

            elif op == 'exit':
                # pass
                BOOL = False
            else:
                print('\033[0;31m无效输入，请检查是否输入为add/delete/update/list/find/exit!\033[0m')
    else:
        print('\033[0;31m登录失败，请重试 !\033[0m')

        logincount += 1
        '''
        此处有bug，2分钟内不要操作键盘，等输入用户名出来再操作。
        
        '''
        if logincount % 3 == 0:
            exit_flag = input('\033[0;34m你已经登录失败3次，要退出吗？（yes/no）:\033[0m')
            if exit_flag == 'yes':
                BOOLEAN = False
            else:
                print('\033[0;31m登录超过3次失败，请2分钟后再试!\033[0m')
                time_second = 120
                count2 = 0
                while count2 < time_second:
                    ncount = time_second - count2
                    time.sleep(1)
                    count2 += 1
