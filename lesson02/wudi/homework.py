import pickle
import os


class User:
    """用户信息"""
    def __init__(self, id, name, age, address):
        self.id = id
        self.name = name
        self.age = age
        self.address = address

class UserService(object):

    __instance = None

    __userList = []

    __maxID = 0

    __pageSize = 20

    __userNameList = []

    def __init__(self, name):
        self.name = name

        if os.path.exists('userList') > 0:
            with open('userList', 'rb') as f:
                self.__userList = pickle.load(f)

        if os.path.exists('userNameList'):
            with open('userNameList', 'rb') as f:
                self.__userNameList = pickle.load(f)
        if os.path.exists('maxID') > 0:
            with open('maxID', 'rb') as f:
                self.__maxID = pickle.load(f)

    @classmethod
    def get_instance(cls):
        if cls.__instance:
            return cls.__instance
        else:
            obj = cls('userservice')
            cls.__instance = obj
            return obj

    def add(self, name, age, address):
        self.__maxID += 1
        user = User(self.__maxID, name, age, address)
        self.__userNameList.append(name)
        self.__userList.append(user)
        print('##################添加成功##################')

    def delete(self, userid):
        for user in self.__userList:
            if user.id == userid:
                self.__userList.remove(user)
                self.__userNameList.remove(user.name)
                break
        print('##################删除成功##################')

    def update(self, userid, name, age, address):
        for user in self.__userList:
            if user.id == userid:
                user.name = name
                user.age = age
                user.address = address
                break
        print('##################修改成功##################')

    def find(self, pageno):
        return self.__userList[(pageno - 1) * self.__pageSize: pageno * self.__pageSize]

    def search(self, searchname):
        results = []
        for user in self.__userList:
            if user.name.count(searchname) > 0:
                results.append(user)
        return results

    def save(self):
        with open('userList', 'wb') as f:
            pickle.dump(self.__userList, f)
        with open('userNameList', 'wb') as f:
            pickle.dump(self.__userNameList, f)
        with open('maxID', 'wb') as f:
            pickle.dump(self.__maxID, f)

    def existsname(self, name):
       return self.__userNameList.count(name) > 0

userservice = UserService.get_instance()

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
            if userservice.existsname(name):
                print('用户名已经存在')
                continue
            if not age.isdigit() or int(age) < 1 or int(age) > 80:
                print('年龄必须在1-80之间')
                continue
            if len(address) < 1:
                print('地址不能为空')
                continue
            userservice.add(name, int(age), address)
        elif option == '2':
            useridstr = input('请输入用户编号:').strip()
            if not useridstr.isdigit():
                print('输入错误')
            userid = int(useridstr)
            userservice.delete(userid)
        elif option == '3':
            useridstr = input('请输入用户编号:').strip()
            name = input('请输入姓名[非空]:').strip()
            age = input('请输入年龄[1-80]:').strip()
            address = input('请输入住址[非空]:').strip()
            if not useridstr.isdigit():
                print('用户编号输入错误')

            if len(name) < 1:
                print('用户名不能为空')
                continue
            if userservice.existsname(name):
                print('用户名已经存在')
                continue
            if not age.isdigit() or int(age) < 1 or int(age) > 80:
                print('年龄必须在1-80之间')
                continue
            if len(address) < 1:
                print('地址不能为空')
                continue

            userid = int(useridstr)
            userservice.update(userid, name, age, address)
        elif option == '4':

            while True:
                pagenostr = input('请输入页码[输入-1返回上一级]:').strip()

                if pagenostr == '-1':
                    break

                if not pagenostr.isdigit():
                    print('请输入正确的数字')
                pageno = int(pagenostr)

                if pageno < 1:
                    break

                results = userservice.find(pageno)
                print('－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
                print('| {:<10} | {:<10} | {:<10} | {:<10} |'.format('编号', '姓名', '年龄', '住址'))
                print('－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
                for user in results:
                    print('| {:<10}  | {:<10} | {:<10}  | {:<10} |'.format(user.id, user.name, user.age, user.address))
                    print('－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
        elif option == '5':
            searchName = input('请输入要搜索的名称:').strip()

            if len(searchName) == 0:
                print('搜索名称不能为空')

            results = userservice.search(searchName)
            print('| {:<10} | {:<10} | {:<10} | {:<10} |'.format('编号', '姓名', '年龄', '住址'))
            for user in results:
                print('| {:<10}  | {:<10} | {:<10}  | {:<10} |'.format(user.id, user.name, user.age, user.address))
                print('－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－')
        else:
            userservice.save()






