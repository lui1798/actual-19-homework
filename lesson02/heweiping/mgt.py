userlist = []
print('-------------------usage---------------------')
print('list: list all users\'s information')
print('add: add a user\'s information')
print('update: update a user\'s information by name ')
print('delete: delete a user\'s information by id')
print('find: find a user\'s information by id or name')

while True:
    op = input('please input action:list or add or update or delete or find or exit ').upper()
    if op == 'LIST':
        # '''
        #     -----------------------------
        #     id name age tel    address
        #     -----------------------------
        #     1 monkey 28 132xxx beijing
        #     1 zhengyscn 21 135xxx shanghai
        #     1 wd 28 131xxx zhengzhou
        #     1 xuegao 28 139xxx shandong
        #     -----------------------------
        # '''
        print('----------------------------------------------------------------------------------------------------')
        print('id'.ljust(4), 'name'.ljust(12), 'age'.ljust(4), 'tel'.ljust(18), 'address'.ljust(20))
        if len(userlist):
            for i in range(len(userlist)):
                print('%-4s%-16s%-4s%-20s%-20s' % (
                    userlist[i][0], userlist[i][1], userlist[i][2], userlist[i][3], userlist[i][4]))
        print('----------------------------------------------------------------------------------------------------')

    elif op == 'ADD':
        # '''
        #     monkey 28 132xxx beijing
        # '''
        lenth = int(len(userlist)) - 1
        if lenth == -1:
            id = 1
        else:
            id = userlist[lenth][0] + 1
        name = input('please input name:')
        age = input('please input age:')
        tel = input('please input telphone:')
        address = input('please input city:')
        userlist.append([id, name, age, tel, address])
        print('Done')
    elif op == 'UPDATE':
        # '''
        #     monkey 28 132xxx beijing
        # '''
        a = input('whose information you want to change:')
        flag1 = 'y'
        flag2 = ''
        for user in userlist:
            while flag1 == 'Y' or flag1 == 'y':
                if a == user[1]:
                    type = input('please input the type you want to change:(name or age or tel or address)').upper()
                    if type == 'NAME':
                        newname = input('please input true name:')
                        user[1] = newname
                    elif type == 'AGE':
                        newage = input('please input true age:')
                        user[2] = newage
                        print('%s\'s age is %s' % (a, newage))
                    elif type == 'TEL':
                        newtel = input('please input true telphone:')
                        user[3] = newtel
                        print('%s\'s tel is %s' % (a, newtel))
                    elif type == 'ADDRESS':
                        newadd = input('please input true address:')
                        user[3] = newadd
                        print('%s\'s address is %s' % (a, newadd))
                    else:
                        print('Input error')
                    flag1 = input('Do you need to continue changing ？y or n (defaut n)')
                    flag2 = 'Got it'
                else:
                    flag1 = 'n'
        if not flag2:
            print('User not found!')

    elif op == 'DELETE':
        # '''
        #     delete 1
        # '''
        flag = ''
        delid = int(input('Please enter the ID number you want to delete:'))
        for user in userlist:
            if delid == user[0]:
                userlist.remove(user)
                flag = 'Got it'
        if not flag:
            print('Input error,Not found')

    elif op == 'FIND':
        # '''
        #     find 1
        #     find monkey
        # '''
        flag = ''
        info = input('Please enter the ID or name you want to query')
        for user in userlist:
            if info == str(user[0]) or info == user[1]:
                print(user)
                flag = 'Got it'
        if not flag:
            print('Input error,Not found')

    elif op == 'EXIT':
        break
    else:
        # 加上颜色 警告信息
        print('\033[1;31m invalid cmd! \033[0m')

userstr = (''.join('%s \n' % id for id in userlist))
file = open('userlist.txt', 'a')
file.write(userstr)
file.close()
print("Logout")