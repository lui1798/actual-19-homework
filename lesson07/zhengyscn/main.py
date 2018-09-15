import os
import sys
import logging

from apps import oper
from apps import login
# from utils import db
# from utils.fmt import Println, PrintTable
from apps.utils.file import ReadConfigFile, WriteExcel


logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                    )


def main():
	BASEDIR = os.path.dirname(os.path.abspath(__file__))
	auth_info, _ = ReadConfigFile(os.path.join(BASEDIR, 'config.ini'), 'AUTH')
	oper.LogicOper()
	
	if auth_info.get('auth_method_for_token') == '1':
		# 基于token认证方式
		token = input("Please input your github token: ").strip()
		msg, ok = login.Auth_login_token(auth_info.get('url'), token)
		logging.debug("msg {}, state {}.".format(msg, ok))
	else:
		username = input("Please input your github username: ").strip()
		password = input("Please input your github password for {}: ".format(username)).strip()
		msg, ok = login.Auth_login_passwd(auth_info.get('url'), username, password)
		logging.debug("msg {}, state {}.".format(msg, ok))
	
	oper.LogicOper()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

if __name__ == '__main__':
	main()
