from utils import log

# 显示表格样式
TABLE_TPL = '|{id:^10}|{username:^10}|{age:^5}|{tel:^15}|{address:^20}|'
TABLE_SPLIT_LINE = 66
TABLE_TITLE = {"id": "id", "username": "username", "age": "age", "tel": "tel", "address": "address"}

# 成功时提示信息
@log.Log_Msg(level="debug")
def SuccMsg(msg):
    print('\033[34m{}\033[0m'.format(msg))


# 错误或警告时提示信息
@log.Log_Msg(level="warn")
def WarnMsg(msg):
    print('\033[31m{}\033[0m'.format(msg))


# 提示用户输入信息函数
def InputMsg(msg):
    data = input("\033[33m{}\033[0m".format(msg)).strip()
    return data


# 显示用户信息函数
def PrintUsers(users):
    print('-' * TABLE_SPLIT_LINE)
    print(TABLE_TPL.format(**TABLE_TITLE))
    print('-' * TABLE_SPLIT_LINE)
    for user in users:
        print(TABLE_TPL.format(**user))
    print('-' * TABLE_SPLIT_LINE)