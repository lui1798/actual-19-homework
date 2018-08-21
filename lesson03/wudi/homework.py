import pickle
import os
import time


class DateUtil(object):

    @staticmethod
    def getstrfmt(pattern):
        return time.strftime(pattern)


class User:
    """用户信息"""
    def __init__(self, id, name, age, address):
        self.id = id
        self.name = name
        self.age = age
        self.address = address


class UserService(object):

    USER_LOGIN_CACHE_KEY = 'user_login_cache_key_'

    USER_LOGIN_FAIL_COUNT = 3

    __instance = None

    __userList = []

    __maxID = 0

    __pageSize = 20

    __userNameList = []

    __cache = {}

    __authinfo = ('admin', 'admin')

    def __init__(self, name):
        self.name = name

        if os.path.exists('database'):
            with open('database', 'rb') as f:
                dic = pickle.load(f)
                self.__userList = dic['userList']
                self.__userNameList = dic['userNameList']
                self.__maxID = dic['maxID']

    @classmethod
    def get_instance(cls):
        if cls.__instance:
            return cls.__instance
        else:
            obj = cls('userservice')
            cls.__instance = obj
            return obj

    def login(self, username, password):
        # 首先验证是否还有机会,一天三次
        cachekey = self.USER_LOGIN_CACHE_KEY + DateUtil.getstrfmt('%Y-%m-%d') + username
        failcount = self.__cache.get(cachekey, 0)
        if failcount >= self.USER_LOGIN_FAIL_COUNT:
            return -1, -1
        elif (username, password) != self.__authinfo:
            failcount += 1
            self.__cache[cachekey] = failcount
            if failcount >= self.USER_LOGIN_FAIL_COUNT:
                return -1, -1
            return 0, (self.USER_LOGIN_FAIL_COUNT - failcount)
        else:
            return 1, 1

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
        dic = {}
        dic['userList'] = self.__userList
        dic['userNameList'] = self.__userNameList
        dic['maxID'] = self.__maxID
        with open('database', 'wb') as f:
            pickle.dump(dic, f)

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
    password = input('请输入密码:')
    ret = userservice.login(username, password)
    if ret[0] == -1:
        print('用户名或密码错误,一天只有三次机会,您没有机会了!')
        exit(0)
    elif ret[0] == 0:
        print('用户名或密码错误,还剩{}次机会!'.format(ret[1]))
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






