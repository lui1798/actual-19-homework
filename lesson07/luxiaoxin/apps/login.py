#-----导入开源模块--------
import getpass
import requests
#-----导入自定义模块--------
from apps.utils.log import success_info,warn_info

#-----定义公用常量-------
#系统管理员用户名和密码，以及Github登录验证的token
ADMIN_NAME = 'admin'
ADMIN_PASSWD = '51@reboot'
TOKEN = "fc75138770b6fe7c7e3a708d44573b05355fa198"
HEADERS = {'Authorization': 'token ' + TOKEN}
HEADERS_ERROR = {'Authorization': 'token '}
#最大登录次数
MAX_LOGIN_COUNT = 3


#--------定义功能函数-------
#判断登录函数
def login():
    is_login = False

    for i in range(MAX_LOGIN_COUNT):
        username = input('请输入用户名:')
        password = getpass.getpass('请输入密码:')

        if username == ADMIN_NAME and password == ADMIN_PASSWD:
            req = requests.get('https://api.github.com/user', headers=HEADERS)
        else:
            req = requests.get('https://api.github.com/user', headers=HEADERS_ERROR)

        if req.ok:
            success_info("管理员登陆成功！")
            print('欢迎管理员登录系统')
            is_login = True
            break
        if MAX_LOGIN_COUNT -1 > i:
            warn_info("管理员用户名或密码有误，错误信息{0}{1}".format(req.status_code, req.reason))
            print('请重新输入用户名,密码!')
        else:
            warn_info("管理员输入的密码错误三次，账号锁定。")
            print('登录失败，锁定用户')
    return is_login
