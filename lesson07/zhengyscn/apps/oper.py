import sys
import logging

from apps.utils import date
from apps.utils import db
from apps.utils.fmt import PrintTable



def add():
	'''
		monkey 18 132xxx beijing
	'''
	userinfo = input("Please input your user info: ")
	userArr = userinfo.split()
	if len(userArr) == 4:
		sql = '''INSERT INTO auth_user(username, age, tel, address, create_time, update_time) VALUES('{}', {}, '{}', '{}', from_unixtime({}), from_unixtime({}));'''.format(*userArr, date.CurrentTimestamp(), date.CurrentTimestamp())
		logging.debug(sql)
		return db.Insert(sql)
	else:
		return "Input args invalid.", False


def delete():
	'''
		1
	'''
	uid = input("Please input your uid: ")
	if uid.isdigit():
		sql = 'DELETE FROM auth_user WHERE id = {};'.format(uid)
		logging.debug(sql)
		return db.Delete(sql)
	else:
		return "Input args invalid.", False


def update():
	'''
	:return:
	'''
	uid = input("Please input your uid: ")
	if uid.isdigit():
		'''name=monkey3, age=20'''
		whereDic = input("Please input your update info: ")
		whereDic = ','.join(["{}='{}'".format(x.split('=')[0].strip(), x.split('=')[1].strip()) for x in whereDic.split(',')])
		sql = 'UPDATE auth_user SET {} WHERE id = {};'.format(whereDic, uid)
		logging.debug(sql)
		return db.Update(sql)
	else:
		return "Input args invalid.", False


def find():
	uid = input("Please input your uid: ")
	if uid.isdigit():
		fields = ['id', 'username', 'age', 'tel', 'address', 'create_time', 'update_time']
		sql = 'SELECT {} FROM auth_user WHERE id = {};'.format(','.join(fields), uid)
		logging.debug(sql)
		msg, ok = db.Select(sql)
		if not ok:
			return 'Select failed', False
		dataMsg = [ dict(zip(fields, x)) for x in msg ]
		responseMsg, _ = PrintTable(dataMsg)
		print(responseMsg)
		return '', True
	else:
		return "Input args invalid.", False

def list():
	fields = ['id', 'username', 'age', 'tel', 'address', 'create_time', 'update_time']
	sql = 'SELECT {} FROM auth_user;'.format(','.join(fields))
	logging.debug(sql)
	msg, ok = db.Select(sql)
	if not ok:
		return 'Select failed', False
	dataMsg = [dict(zip(fields, x)) for x in msg]
	responseMsg, _ = PrintTable(dataMsg)
	print(responseMsg)
	return '', True

def quit():
	sys.exit(-1)


def LogicOper():
	prompt = "\nMenu: \n\tadd:\n\tupdate:\n\tfind:\n\tlist:\n\texit:\n\tPlease input your action:  "
	mapFunc = {'add' : add, 'delete' : delete, 'update' : update, 'find' : find, 'list' : list,  'quit' : quit}

	while 1:

		op = input(prompt).strip()
		print('---{}---'.format(op))
		try:
			mapFunc[op]()
		except Exception as e:
			logging.warning("Invalid op, please try again.")
		# if op == 'add':
		# 	response, ok = add()
		# 	if ok:
		# 		logging.info("Add sucess.")
		# 	else:
		# 		logging.warning("Add failed.")
		# elif op == 'delete':
		# 	response, ok = delete()
		# 	if ok:
		# 		logging.info("Delete sucess.")
		# 	else:
		# 		logging.warning("Delete failed.")
		# elif op == 'update':
		# 	response, ok = update()
		# 	if ok:
		# 		logging.info("Update sucess.")
		# 	else:
		# 		logging.warning("Update failed.")
		# elif op == 'find':
		# 	response, ok = find()
		# 	if ok:
		# 		logging.info("Find sucess.")
		# 	else:
		# 		logging.warning("Find failed.")
		# elif op == 'list':
		# 	list()
		# elif op == 'exit':
		# 	exit()
		# else:
		# 	logging.warning("Invalid op, please try again.")


def LogicOperSwithCase():
	mapFunc = {'add' : add, 'delete' : delete, 'update' : update, 'list' : list}
	while 1:
		op = input("Please input your action: ").strip()
		try:
			mapFunc[op]('1')
		except:
			logging.warning("Invalid op, please try again.")


		# if op == 'add':
		# 	add()
		# elif op == 'delete':
		# 	pass
		# elif op == 'update':
		# 	pass
		# elif op == 'find':
		# 	pass
		# elif op == 'list':
		# 	pass
		# elif op == 'exit':
		# 	sys.exit(0)
		# else:
		# 	logging.warning("Invalid op, please try again.")