user_info = []
login_info = ('admin','123456')
count  = 0
admin_pass = 0
go_on = '\033[36m输入回车继续操作\033[0m'

#用户名登陆
while True:
    username = input("enter your username: ")
    password = input("enter your pass: ")
    if username == login_info[0] and password == login_info[1] :
        admin_pass = 1
        break   #跳出第一个while，并赋值pass
    else :
        print('\033[31mYour password is wrong.\033[0m')
        count += 1
        if count > 2:
            print('\033[31mYou have no chances today\033[0m', end=' ')
            break

while True:
    if admin_pass == 1 :
        op = input('''\033[32m
                      #Choose Number#
            ************************************
                          add:1
                          delete:2
                          find:3
                          update:4
                          list:5
                          exit:q
            ************************************
        Your choose:\033[0m''')

        # add操作命令行：1> 格式化输入信息 ；2>以列表形式输出；3>给予序号
        if op == '1':
            name = input('enter your name:\n')
            age = input('enter your age:\n')
            tel = input('enter your tel:\n')
            address = input('enter your address:\n')
            new_info = "{} {} {} {}".format(name,age,tel,address)
            # print(new_info)
            user_add = new_info.split()
            # print(user_add)
            if len(user_info) == 0:
                user_add.insert(0,1)
                user_info.append(user_add)
            else:
                user_id = [x[0] for x in user_info] #遍历user_info的每一个value，取value的[0]
                new_id = max(user_id) + 1
                user_add.insert(0,new_id)
                user_info.append(user_add)
            print('''\033[34m
            Add Over,your information  :
            ****************************
            name:{}
            age:{}
            tel:{}
            address:{}
            ****************************
            \033[0m'''.format(name,age,tel,address))
            input(go_on)
            # print(user_info)

        # delete操作命令行：1> 输入序号删除信息
        elif op == '2':
            id_del = int(input('del which one ：'))
            for x in user_info:
                if x[0] == id_del:
                    user_info.remove(x)
            print('''\033[34mDel Over,your information del.\033[0\n''')
            input(go_on)

        # find操作命令行：1> 输入查询关键词；2> 遍历寻找匹配；3>输出匹配行
        elif op == '3':
            a = 0
            name_find = input('please enter your find infornamtion: ')
            for x in user_info:
                    for y in x:
                        if y == name_find:
                            print(x)
                            a = 1
            if a == 0:
                print("\033[31m  We find nothing ...  \033[0m")
            input(go_on)

        # update修改操作：1>输入要修改的id； 2>打印id所在行； 3>想修改的属性
        elif op == '4':
           up_index = int(input("你想修改哪一个序号的信息? :\n"))
           user_up = []
           a = 0
           # print(user_info) #测试输出
           for x in user_info:
               if x[0] == up_index:
                   print("此序号目前的信息为: \n",x)
                   #新参数
                   a_up = int(input("\n您想修改哪个属性:(name:输入1/age:2/tel:3/address:4)\n"))
                   while True:
                        if a_up == 1:
                            x[1] = input('enter your new name:\n')
                            break
                        elif a_up == 2:
                            x[2] = input('enter your new age:\n')
                            break
                        elif a_up == 3:
                            x[3] = input('enter your new tel:\n')
                            break
                        elif a_up == 4:
                            x[4] = input('enter your new address:\n')
                            break
                        else:
                            print("\033[31m输入信息有误，请重新输入：\033[0m")
                            a_up = int(input())

                   user_up = x
           print("\033[34m修改后：{}\033[0m".format(user_up))
           input(go_on)

        # list打印目前列表：1< 遍历格式化输出
        elif op == '5':
            print('''\033[34m
-------------------------------------------
id      name    age     tel         address
-------------------------------------------\033[0m''')
            for x in user_info:
                print(x[0],'    ',x[1],'    ',x[2],'    ',x[3],'    ',x[4])
            input(go_on)

        #退出
        elif op == 'q':
            break
    #如果三次用户登录错误，直接跳到第二个while的break
    else:
        break



