import requests
from apps.utils.file import *

def Get(url, params=None, headers=None):
    '''
        url http://rebootapi.51reboot.com/api/v1/users/1
    :param url:
    :param params:
    :param headers:
    :return:
    '''
    if params:
        req = requests.get(url, params=params)
    elif headers:
        req = requests.get(url, headers=headers)
    else:
        req = requests.get(url)
    # print(req.status_code)
    if req.ok:
        return req.json(), True
    else:
        return req.text, False


def GetAuth(url, usrename, password):
    req = requests.get(url, auth=(usrename, password))
    # print(req.status_code)
    if req.ok:
        return req.json(), True
    else:
        return req.text, False