import time
import json

import getpass
import requests

import db
import utils

#管理员登录锁定时长
LOCK_INTERVAL=30
#系统管理员用户和github的token
ADMIN_NAME='admin'
ADMIN_PASSWD='51reboot'
TOKEN="000"
TOKEN={'Authorization': 'token ' + TOKEN'}

#
MAX_LOGIN_COUNT=4
USER_INFO=('id','name',)
#再测试一下

