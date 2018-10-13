import os
import sys
import logging

from apps import oper
from apps import login
from apps.utils.file import ReadConfigFile


logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                    )


def main():
	BASEDIR = os.path.dirname(os.path.abspath(__file__))
	auth_info, _ = ReadConfigFile(os.path.join(BASEDIR, 'config.ini'), 'AUTH')

	# if auth_info.get('auth_method_for_token') == '1':
	# 	token = input("Please input your github token: ").strip()
	# 	msg, ok = login.Auth_login_token(auth_info.get('url'), token)
	# else:
	# 	username = input("Please input your github username: ").strip()
	# 	password = input("Please input your github password for {}: ".format(username)).strip()
	# 	msg, ok = login.Auth_login_passwd(auth_info.get('url'), username, password)
	#
	# if not ok:
	# 	logging.error("Auth error.")
	# 	sys.exit(1)

	oper.LogicOper()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

if __name__ == '__main__':
	main()
