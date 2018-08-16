# @Time    : 2018-8-15
# @Author  : mayulei
'''
用户管理系统：
1、登录认证；
2、增删改查；
3、格式化输出。

系统中存储用户信息如下：
id        name            tel             addr
1 	 	 mayulei 	 	  132xxx 	 	 shandong
2 	 	 wangqianong 	  132xxx         henan
...
'''
import time
password_list = ['admin','123456'] # 用户名密码
user_list = [
    [1, 'mayulei',       '188xxx', 'shandong'],
    [2, 'pangya',        '188xxx', 'henan'    ],
    [3, 'wangqianlong', '188xxx', 'henan'    ],
    [4, 'haoshan',       '188xxx', 'hebei'    ],
]
option_list=['0','1','2','3','4','5']
count = 3 #错误登录次数
display_info='''
操作列表：
0、显示已有用户信息
1、增加用户信息
2、删除用户信息
3、修改用户信息
4、查询用户信息
5、退出系统
'''

while count > 0:
    login = input('请输入用户名:')
    password = input('请输入密码:')
    if login == 'admin'  and password == '123456':
        break
    elif count - 1 == 0:
        print('\033[31m输入用户名密码错误3次，用户被锁定\033[0m')
        time.sleep(60)
        count = 3
    else:
        print('\033[31m用户名或密码错误，还有{}次机会\033[0m'.format(count - 1))
        count -= 1


print('\033[33m欢迎用户' + 'login' + '登录系统\033[0m')

while True:
    print(display_info)
    option = input('请选择对应操作：')
    if option in option_list:
        if option == option_list[0]:
            print('\033[34m{:<5}{:<15}{:<15}{:<15}\033[0m'.format('ID','name','tel','addr'))
            for x in user_list:
                print('\033[33m{:<5}{:<15}{:<15}{:<15}\033[0m'.format(x[0],x[1],x[2],x[3],))
        elif option == option_list[1]:
            input_info = input('请按照以下格式输入用户信息： name tel address :')
            user_info = input_info.split(' ')  # 将输入的字符串，按空格分隔
            if len(user_list) == 0:  # 如果原有用户信息列表为空
                user_info.insert(0, 1)  # 列表第0个未知，插入数值1
                user_list.append(user_info)  # 将输入的信息加到id 1 后面
                print("\033[32m用户已添加\033[0m")
            else:
                id_list = [x[0] for x in user_list]  # 列表推导式 第0个元素组成个新列表
                new_id = max(id_list) + 1  #新的id是最大的+1
                user_info.insert(0, new_id) #在列表第0个违章插入新id
                user_list.append(user_info)
                print("\033[32m用户已添加\033[0m")
                print('\033[34m{:<5}{:<15}{:<15}{:<15}\033[0m'.format('ID', 'name', 'tel', 'addr'))
                print('\033[33m{:<5}{:<15}{:<15}{:<15}\033[0m'.format(user_list[-1][0], user_list[-1][1], user_list[-1][2], user_list[-1][3], ))
        elif option == option_list[2]:
            user_id = input('输入要删除的用户ID:')
            id_list = [str(x[0]) for x in user_list]
            if user_id in id_list:
                for x in user_list:
                    if x[0] == int(user_id):
                        user_list.remove(x)
                        print("\033[32m用户已删除\033[0m")
            else:
                print("\033[31m无此ID用户\033[0m")
        elif option == option_list[3]:
            user_id = input('请输入需要修改信息的用户ID:')
            id_list = [str(x[0]) for x in user_list]  # 列表推导式 第0个元素组成个新列表
            if  user_id in id_list:
                for x in user_list:
                    if x[0] == int(user_id):
                        while True :
                            user_info = input('请输入需要修改的内容（name/tel/addr）:')
                            if user_info == 'name':
                                user_name = input('请输入新用户名:')
                                x[1] = user_name
                                print("\033[32m用户名修改成功\033[0m")
                                #print(x)
                                update_flag = input('是否继续修改（y/n）:')
                                if update_flag == 'y':
                                    continue
                                else:
                                    break
                            elif user_info == 'tel':
                                user_tel = input('请输入新手机号:')
                                x[2] = user_tel
                                print("\033[32m手机号修改成功\033[0m")
                                #print(x)
                                update_flag = input('是否继续修改（y/n）:')
                                if update_flag == 'y':
                                    continue
                                else:
                                    break
                            elif user_info == 'addr':
                                user_add = input('请输入新地址:')
                                x[3] = user_add
                                print("\033[32m手机号修改成功\033[0m")
                                #print(x)
                                update_flag = input('是否继续修改（y/n）:')
                                if update_flag == 'y':
                                    continue
                                else:
                                    break
                            else :
                                print("\033[32m输入错误\033[0m")
                                update_flag = input('是否放弃修改（y/n）:')
                                if update_flag == 'y':
                                    break
                        break
            else:
                print("\033[31m无此ID用户\033[0m")

        elif option == option_list[4]:
            input_info = input('请输入，查找关键字 :')
            find_list = []
            for user_x in user_list:
                if input_info in user_x:
                    find_list.append(user_x)
            if len(find_list)!= 0:
                print('\033[32m查找的用户信息如下：\033[0m')
                print('\033[34m{:<5}{:<15}{:<15}{:<15}\033[0m'.format('ID', 'name', 'tel', 'addr'))
                for x in find_list:
                    print('\033[33m{:<5}{:<15}{:<15}{:<15}\033[0m'.format(x[0], x[1], x[2], x[3], ))
            else:
                print('\033[31m未有相关用户\033[0m')
        elif option == option_list[5]:
            break

print('\033[32m您已退出系统\033[0m')
