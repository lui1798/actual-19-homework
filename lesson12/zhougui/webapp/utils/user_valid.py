#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @File  : user_valid.py
# @Author: ZhouGui
# @Date  : 2018/11/11
# @Description :
def valid_userinfo(jsondata):
    '''
    如果返回True， 表明验证成功， 否则验证失败；
    :param jsondata: json
    :return: str, bool
    '''
    if isinstance(jsondata, dict):
        for k, v in jsondata.items():
            if v == "":
                return "key {}, value is required.".format(k), False

        if 'sex' in jsondata:
            sex = jsondata.get('sex')
            if sex.isdigit() and sex in ['0', '1']:
                pass
            else:
                return "sex params is invalid.", False
    return "", True
