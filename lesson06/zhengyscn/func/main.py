import os
import sys
import logging

from utils import db
from utils.fmt import Println, PrintTable
from utils.file import ReadConfigFile, WriteExcel


def main():
	logging.basicConfig(level=logging.DEBUG,
	                    format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
	                    filename='/var/log/agent.log',
	                    filemode='a'
	                    )
	'''
	# Insert
	insert_sql = "INSERT INTO user(username, age, tel, address) VALUES('monkey1', 18, '132xxx', 'beijing')"
	msg, ok = db.Insert(insert_sql)
	if not ok:
		logging.warning("msg {}.".format(msg))
	'''
	
	'''
	# Select
	fields = ['username', 'age', 'tel', 'address']
	select_sql = "SELECT {} FROM user;".format(','.join(fields))
	msg, ok = db.Select(select_sql)
	if not ok:
		logging.warning("msg {}.".format(msg))
		
	select_msg = [ dict(zip(fields, x)) for x in msg ]
	Println(select_msg)
	'''
	
	'''
	uid = 2
	delete_sql = "DELETE FROM user WHERE id = {};".format(uid)
	msg, ok = db.Delete(delete_sql)
	if not ok:
		logging.warning("msg {}.".format(msg))
	print(msg)
	'''
	
	# data = [
	# 	{'id': 1, 'name': 'monkey1', 'age': 18, 'tel': '132xxx', 'address': 'beijing'},
	# 	{'id': 2, 'name': 'monkey2', 'age': 18, 'tel': '132xxx', 'address': 'beijing'},
	# 	{'id': 3, 'name': 'monkey3', 'age': 18, 'tel': '132xxx', 'address': 'beijing'},
	# ]
	
	# data1 = {'id': 1, 'name': 'monkey1', 'age': 18, 'tel': '132xxx', 'address': 'beijing'}
	# table_msg, ok = PrintTable(data1)
	# print(table_msg)
	
	# WriteExcel('python19.xls', data)


if __name__ == '__main__':
	main()
