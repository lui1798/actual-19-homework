import pickle
import os

class User:
    """用户信息"""
    def __init__(self, id, name, age, address):
        self.id = id
        self.name = name
        self.age = age
        self.address = address


pageSize = 20

userList = []
if os.path.exists('userList') > 0:
    with open('userList', 'rb') as f:
        userList = pickle.load(f)

userNameList = []

if os.path.exists('userNameList'):
    with open('userNameList', 'rb') as f:
        userNameList = pickle.load(f)

maxID = 0
if os.path.exists('maxID') > 0:
    with open('maxID', 'rb') as f:
        maxID = pickle.load(f)

print(userList, userNameList, maxID)

print('#########################################')
print('#                                       #')
print('#        欢迎登录51reboot人员管理系统       #')
print('#                                       #')
print('#########################################')
while True:
    username = input('请输入用户名:')
    pasword = input('请输入密码:')
    if username != 'admin' or pasword != 'admin':
        print('用户名或密码错误!')
        continue

    print('#########################################')
    print('#                                       #')
    print('#        请选择编号:                      #')
    print('#        [1]添加                         #')
    print('#        [2]删除                         #')
    print('#        [3]修改                         #')
    print('#        [4]查询                         #')
    print('#        [5]搜索                         #')
    print('#        [6]退出                         #')
    print('#        [7]保存                         #')
    print('#########################################')
    while True:
        option = input('请选择编号:')
        if not option.isdigit() or int(option) > 7 or int(option) < 1:
            print('编号输入错误,请重新输入')
            continue
        if option == '6':
            print('谢谢,再见!')
            exit()
        elif option == '1':
            name = input('请输入姓名[非空]:').strip()
            age = input('请输入年龄[1-80]:').strip()
            address = input('请输入住址[非空]:').strip()
            if len(name) < 1:
                print('用户名不能为空')
                continue
            if userNameList.count(name) > 0:
                print('用户名已经存在')
                continue
            if not age.isdigit() or int(age) < 1 or int(age) > 80:
                print('年龄必须在1-80之间')
                continue
            if len(address) < 1:
                print('地址不能为空')
                continue
            maxID += 1
            userNameList.append(name)
            user = User(maxID, name, int(age), address)
            userList.append(user)
            print('##################添加成功##################')
        elif option == '2':
            userIDStr = input('请输入用户编号:').strip()

            if not userIDStr.isdigit():
                print('输入错误')

            userID = int(userIDStr)
            for user in userList:
                if user.id == userID:
                    userList.remove(user)
                    userNameList.remove(user.name)
                    break
            print('##################删除成功##################')
        elif option == '3':
            userIDStr = input('请输入用户编号:').strip()
            name = input('请输入姓名[非空]:').strip()
            age = input('请输入年龄[1-80]:').strip()
            address = input('请输入住址[非空]:').strip()
            if not userIDStr.isdigit():
                print('用户编号输入错误')

            if len(name) < 1:
                print('用户名不能为空')
                continue
            if userNameList.count(name) > 0:
                print('用户名已经存在')
                continue
            if not age.isdigit() or int(age) < 1 or int(age) > 80:
                print('年龄必须在1-80之间')
                continue
            if len(address) < 1:
                print('地址不能为空')
                continue

            userID = int(userIDStr)
            for user in userList:
                if user.id == userID:
                    user.name = name
                    user.age = age
                    user.address = address
                    break
            print('##################修改成功##################')
        elif option == '4':

            while True:
                pageNoStr = input('请输入页码:').strip()
                if not pageNoStr.isdigit():
                    print('请输入正确的数字')
                pageNo = int(pageNoStr)

                if pageNo < 1:
                    print('请输入大于1的页码')
                print('－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
                print('| {:<10} | {:<10} | {:<10} | {:<10} |'.format('编号', '姓名', '年龄', '住址'))
                print('－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
                for user in userList[(pageNo - 1) * pageSize: pageNo * pageSize]:
                    print('| {:<10}  | {:<10} | {:<10}  | {:<10} |'.format(user.id, user.name, user.age, user.address))
                    print('－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
        elif option == '5':
            searchName = input('请输入要搜索的名称:').strip()

            if len(searchName) == 0:
                print('搜索名称不能为空')
            print('| {:<10} | {:<10} | {:<10} | {:<10} |'.format('编号', '姓名', '年龄', '住址'))
            for user in userList:
                if user.name.count(searchName) > 0:
                    print('| {:<10}  | {:<10} | {:<10}  | {:<10} |'.format(user.id, user.name, user.age, user.address))
                    print('－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
            print('##################搜索成功##################')
        else:
            with open('userList', 'wb') as f:
                pickle.dump(userList, f)
            with open('userNameList', 'wb') as f:
                pickle.dump(userNameList, f)
            with open('maxID', 'wb') as f:
                pickle.dump(maxID, f)






