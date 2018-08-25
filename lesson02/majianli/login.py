user = [[1, 'zhangsan', 18, '1111111111', 'beijing'], [2, 'lisi', 18, '1111111111', 'beijing']]
number =1
username = 'admin'
password = '123456'
list_tmp = []


while number < 4:



    if number == 3:
        print('第{}次，最后一次机会' .format((number)))
    manager_user = input('manager_user:')
    manager_pass = input('manager_pass:')
    if  manager_user == username and manager_pass == password:
        print("\033[1;32mlogin sessfull\033[0m")
        while True:
            action = input('Please input action:')
            if action == '--help':
                print('''
                    help:帮助信息
                    list:显示全部
                    add：添加
                    del: 删除
                    update：更新
                    find：查找
                    exit：退出
                ''')
            elif action == 'list':
                for i in user:
                    for x in i:
                        print(x, '\t', end=' ')
                    print()
            elif action == 'add':
                for j in user:
                    list_tmp.append(j[0])
                max_id = max(list_tmp) + 1
                infor = input('Please input information(format：name age mobile addr ):')
                list_temp2 = []
                list_temp2.append(max_id)
                list_temp2.extend(infor.split())
                user.append(list_temp2)
                print('\033[1;32muser {} add successful\033[0m'.format(list_temp2[1]))
            elif  action == 'update':
                while True:
                    list_temp3 = []
                    input_id = int(input('Input will change Id :'))
                    for l in user:
                        list_temp3.append(l[0])
                    if input_id in list_temp3:
                        new_user = input('Input new_userinfor message (formats：name age mobile addr ):').split()
                        for kk in user:
                            if kk[0] == input_id:
                                kk[1] = new_user[0]
                                kk[2] = new_user[1]
                                kk[3] = new_user[2]
                                kk[4] = new_user[3]
                                print('\033[1;32mid {} 更新成功\033[0m'.format(input_id))
                        go_on = input('是否还要更新（y or n）:')
                        if go_on == ('y' or 'Y'):
                            continue
                        else:
                            break
            elif action == 'delete':

                while True:
                    input_del = int(input('删除ID:'))
                    list_temp4 = []
                    for ii in user:
                        list_temp4.append(ii[0])
                    if input_del in list_temp4:
                        for i in user:
                            if input_del == i[0]:
                                user.remove(i)
                                print('id {} 已被删除'.format(input_del))
                                break
                    else:
                        print('无此id')
                        break
                    go_on_1 = input('是否还要删除（y or n）:')
                    if go_on_1 == ('y' or 'Y'):
                        continue
                    elif go_on_1 == ('n' or 'N'):
                        break
                    else:
                        input('输入有误,请重新输入！(y or n)')
                        continue
            elif action == 'find':
                find_input= (input('输入要查找的ID或NAME:'))
                if find_input.isdigit():
                    for i in user:
                        if int(find_input) == i[0]:
                            print(str(i).strip("[]"),end=' ')
                            print()
                else:
                    for i in user:
                        if find_input == i[1]:
                            print(str(i).strip("[]"),end=' ')
                            print()
                go_on = input('是否要继续（y or n）:')
                if go_on == ('y' or 'Y'):
                    continue
                elif go_on == ('n' or 'N'):
                    break
                else:
                    input('输入有误,请重新输入！(y or n)')
            else:
                print("\033[31mInvalid command\033[0m" )
    else:
        print("\033[31m Invalid username and password\033[0m")
        number += 1


