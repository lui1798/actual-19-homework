import sys
import logging

from apps.utils import date
from apps.utils import db



def add():
	'''
		monkey 18 132xxx beijing
	'''
	userinfo = input("Please input your user info: ")
	userArr = userinfo.split()
	if len(userArr) == 4:
		sql = '''INSERT INTO auth_user('username', 'age', 'tel', 'address', 'create_time', 'updatetime') VALUES('{}', {}, '{}', '{}', from_unixtime({}), from_unixtime({}));'''.format(*userArr, date.CurrentTimestamp(), date.CurrentTimestamp())
		logging.debug(sql)
		return db.Insert(sql)
	else:
		return "Input args invalid.", False


def delete():
	pass


def update():
	pass


def find():
	pass

def list():
	pass


def LogicOper():
	while 1:
		op = input("Please input your action: ").strip()
		if op == 'add':
			add()
		elif op == 'delete':
			pass
		elif op == 'update':
			pass
		elif op == 'find':
			pass
		elif op == 'list':
			pass
		elif op == 'exit':
			sys.exit(0)
		else:
			logging.warning("Invalid op, please try again.")