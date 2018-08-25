#本次作业具体实现：

#①连续失败3次，账户锁定，24小时后可以重新登陆！

#②输入失败一次后登陆成功，失败次数恢复为3次。

#③正常登陆成功，执行增删改查，主要实现分页功能，字典结构显示。

#④实现持久化功能。

import json
import datetime

logininfo = ('admin', '51reboot') #登陆用户名密码

# 登录成功界面
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

logincount = 1  # count  次数限制3次，连续3次密码错误，第二天后再登
while True:
    username = input('\033[0;34m请输入用户名:\033[0m')
    password = input('\033[0;34m请输入密码:\033[0m')
    username = username.strip()
    password = password.strip()

    if username == logininfo[0]:
        cur_time = datetime.datetime.now()
        try:
            fd_time = open('time.txt', 'r')
            membuf_time = fd_time.read()
            membuf_time = json.loads(membuf_time)
            membuf_time = datetime.datetime.strptime(membuf_time, '%Y-%m-%d %H:%M:%S')
            fd_time.close()
            cur_time = cur_time + datetime.timedelta(days=-1)
        except FileNotFoundError:  #文件未找到的话置membuf_time初值
            membuf_time = cur_time
        if membuf_time <= cur_time:

            while logincount < 4:
                if password == logininfo[1]:
                    logincount = 1  #每次登陆成功，置1，登陆次数恢复为3次
                    # print('\033[0;32;40m登录成功!\033[0m')
                    print(login_sucess)
                    try:
                        fd = open('userinfo.txt', 'r')
                        membuf_userinfo = fd.read()
                        # print(type(membuf_userinfo))
                        userinfo = json.loads(membuf_userinfo)
                        fd.close()
                    except FileNotFoundError: #找不到文件定义空列表。
                        userinfo = []
                    # 以下循环执行增删改查操作

                    while True:
                        op = input('\033[0;34m请输入操作方式(add/delete/update/list/find/exit) :\033[0m')
                        if op == 'add':
                            userinfo_input = input('\033[0;34m请输入用户信息(格式name age tel address):\033[0m')
                            '''
                            实现增操作，将输入信息转为字典格式存储在列表中。
                            '''
                            userinfo_list = userinfo_input.split(' ')
                            userinfo_dic = {}
                            userinfo_dic['userid'] = ' '
                            userinfo_dic['name'] = userinfo_list[0]
                            userinfo_dic['age'] = int(userinfo_list[1])
                            userinfo_dic['tel'] = userinfo_list[2]
                            userinfo_dic['address'] = userinfo_list[3]
                            # print(userinfo_dic)
                            if len(userinfo_list) == 4:
                                if len(userinfo) == 0:
                                    # userinfo_list.insert(0, 1)
                                    userinfo_dic['userid'] = 1
                                    userinfo.append(userinfo_dic)
                                    print('\033[0;33m添加成功，可以通过list查看！\033[0m')
                                else:
                                    '''
                                    查重功能：不重复则添加，重复则报错
                                    '''
                                    BOOL0 = False
                                    for x in userinfo:
                                        if list(x.values())[1:] == list(userinfo_dic.values())[1:]:
                                            BOOL0 = True
                                    if BOOL0 == False:
                                        uids = [x['userid'] for x in userinfo]
                                        new_id = max(uids) + 1

                                        userinfo_dic['userid'] = new_id
                                        userinfo.append(userinfo_dic)
                                        print('\033[0;33m添加成功，可以通过list查看！\033[0m')
                                    else:
                                        print('\033[0;33m用户已存在，请重新添加！\033[0m')
                            else:
                                print('\033[0;31m未按格式要求输入!\033[0m')
                            # print(userinfo)
                        elif op == 'delete':
                            # 实现：按用户ID删除整个用户信息，且用户ID一旦建立不可更改，标识唯一用户；
                            if len(userinfo) != 0:
                                uid = int(input('\033[0;34m请输入用户ID:\033[0m'))
                                if uid in [x['userid'] for x in userinfo]:
                                    for x in userinfo:
                                        if x['userid'] == uid:
                                            userinfo.remove(x)
                                else:
                                    print('\033[0;33m用户ID不存在，请通过搜索找到用户ID再尝试删除！\033[0m')
                            else:
                                print('\033[0;31m用户信息列表为空，不能删除!\033[0m')

                        elif op == 'update':
                            # pass
                            '''
                             实现：根据用户ID修改用户年龄或电话或地址信息
                            '''
                            if len(userinfo) != 0:
                                uidd = int(input('\033[0;34m请输入用户ID：\033[0m'))
                                if uidd in [x['userid'] for x in userinfo]:
                                    updateinfo = input('\033[0;34m请输入要修改的信息(age/tel/addr):\033[0m')
                                    if updateinfo == 'age':
                                        updateinfo_after = int(input('\033[0;34m请输入修改后年龄:\033[0m'))
                                        for x in userinfo:
                                            if x['userid'] == uidd:
                                                x['age'] = updateinfo_after
                                        print('\033[0;33m修改成功，可以通过list查看！\033[0m')
                                    elif updateinfo == 'tel':
                                        updateinfo_after = input('\033[0;34m请输入修改后电话:\033[0m')
                                        for x in userinfo:
                                            if x['userid'] == uidd:
                                                x['tel'] = updateinfo_after
                                        print('\033[0;33m修改成功，可以通过list查看！\033[0m')
                                    elif updateinfo == 'addr':
                                        updateinfo_after = input('\033[0;34m请输入修改后地址:\033[0m')
                                        for x in userinfo:
                                            if x['userid'] == uidd:
                                                x['address'] = updateinfo_after
                                        print('\033[0;33m修改成功，可以通过list查看！\033[0m')
                                    else:
                                        print('\033[0;31m无效输入，请检查是否输入的age/tel/addr!\033[0m')
                                else:
                                    print('\033[0;33m用户ID不存在，请尝试通过搜索找到用户ID再进行修改！\033[0m')
                            else:
                                print('\033[0;31m用户信息列表为空，无需修改，请尝试添加用户!\033[0m')

                        elif op == 'list':
                            '''
                            实现：分页显示当前用户信息列表中存在的所有用户；
                            '''
                            if len(userinfo) == 0:
                                print('\033[0;31m当前用户列表信息为空！\033[0m')
                            else:
                                page_size = 5
                                userinfo_len = len(userinfo)

                                # 计算页数
                                if userinfo_len % page_size == 0:
                                    page_count = int(userinfo_len / page_size)
                                else:
                                    page_count = int(userinfo_len / page_size) + 1

                                if page_count == 1:
                                    print('\033[0;33m第1页，共1页：\033[0m')
                                    for x in userinfo:
                                        print(x)
                                else:
                                    count1 = 1
                                    while count1 <= page_count:
                                        print('\033[0;33m第 {} 页 ， 共 {} 页 \033[0m'.format(count1, page_count))
                                        count2 = (count1 - 1) * page_size
                                        userinfo_list_page = userinfo[count2:count2 + page_size]
                                        for i in userinfo_list_page:
                                            print(i)
                                        nextorback = input('\033[0;33m请输入next或back进行翻页,也可以选择exit退出翻页：\033[0m')
                                        if nextorback == 'next' or nextorback == 'back':
                                            if nextorback == 'next':
                                                count1 += 1
                                                if count1 == page_count + 1:
                                                    print('\033[0;33m最后一页，请尝试返回！\033[0m')
                                                    count1 = page_count
                                            elif nextorback == 'back':
                                                count1 -= 1
                                                if count1 == 0:
                                                    count1 = 1
                                                    print('\033[0;33m已返回首页，请尝试下翻！\033[0m')
                                        elif nextorback == 'exit':
                                            break
                                        else:
                                            print('\033[0;31m输入错误,请检查！\033[0m')
                        elif op == 'find':
                            '''
                            实现：通过输入搜索关键字实现搜索功能；
                            '''
                            findsome = []
                            keywordinfo = input('\033[0;34m请输入搜索关键字（不大于5个，空格隔开）：\033[0m')
                            keyword_list = keywordinfo.split(' ')
                            # keyword_list[0] = int(keyword_list[0])
                            # keyword_list[2] = int(keyword_list[2])
                            for x in userinfo:
                                value_list = list(x.values())
                                value_list[0] = str(value_list[0])
                                value_list[2] = str(value_list[2])
                                i = 0
                                BOOL2 = True
                                while i < len(keyword_list):
                                    if keyword_list[i] in value_list:
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
                                    print('\033[0;32m{0:^5d}{1:>10s}{2:^10d}{3:^10s}{4:^10s}\033[0m'.format(x['userid'], x['name'], x['age'], x['tel'],
                                                                                                            x['address']))

                        elif op == 'exit':
                            # pass
                            fd = open('userinfo.txt', 'w')
                            membuf_userinfo = json.dumps(userinfo)
                            fd.write(membuf_userinfo)
                            fd.close()
                            break
                        else:
                            print('\033[0;31m无效输入，请检查是否输入为add/delete/update/list/find/exit!\033[0m')
                    break
                else:
                    print('\033[0;31m登录失败{}次，共3次，请重试 !\033[0m'.format(logincount))
                    logincount += 1
                    if logincount == 4:
                        print('已失败3次登录，请明天再试！')
                        cur_time = datetime.datetime.now()
                        cur_time = cur_time.strftime('%Y-%m-%d %H:%M:%S')
                        fd_time = open('time.txt', 'w')
                        membuf_time = json.dumps(str(cur_time))
                        fd_time.write(membuf_time)
                        fd_time.close()
                    else:
                        break
        else:
            diff = membuf_time - cur_time
            diff = diff.seconds / 3600
            print('\033[0;31m此账户还在锁定，请 {} 小时后再试!\033[0m'.format(round(diff, 2)))

    else:
        print('\033[0;31m此账户不存在，请检查输入或选择退出！\033[0m')
        exit_sys = input('\033[0;33m输入yes选择退出：\033[0m')
        if exit_sys =='yes':
            break
        else:
            continue

