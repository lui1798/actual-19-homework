import os
import sys
import logging

from apps import oper
from apps.login import *
from apps.utils.msg import *


def main():
    # 账号被锁定
    if IsLock():
        sys.exit()

    # 登陆操作，成功后进行相关操作
    if Login():
        oper.LogicOper()

if __name__ == '__main__':
    main()
