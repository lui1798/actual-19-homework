from apps.utils.http import Get, GetAuth



def IsLock():
	pass


def Auth_login_token(url, token):
	headers = {'Authorization' : 'Token {}'.format(token) }
	return Get(url, headers=headers)


def Auth_login_passwd(url, username, password):
	return GetAuth(url, username, password)