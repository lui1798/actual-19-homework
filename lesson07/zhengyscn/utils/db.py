import pymysql


'''
	Build connect
'''
def connect(host, user, passwd, db):
	kwargs = {
		'host' : 'localhost',
		'user' : 'user',
		'passwd' :'passwd',
		'db': 'db',
	}
	return pymysql.connect(**kwargs)


def Select():
	connect()


def Insert():
	pass


def Update():
	pass


def Delete():
	pass