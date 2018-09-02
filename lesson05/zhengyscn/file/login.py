import datetime
from decorator import decoratorFunc


@decoratorFunc
def UserLogin(username, password):
    # print('__name__', UserLogin.__name__)
    # print('User login')
    # print(username, password)
    return True



UserLogin('admin', '123456')