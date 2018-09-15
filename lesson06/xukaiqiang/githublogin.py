#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/14 下午10:07
# @Author  : iteemo
# @File    : githublogin.py
import requests

from lxml import etree

class Githublogin():
    def __init__(self):
        self.log_url = 'https://github.com/login'
        self.session_url = 'https://github.com/session'
        self.repo_url = 'https://github.com/settings/repositories'
        self.is_status = False
        self.session = requests.session()
        # self.response = self.session.get(self.log_url, headers=self.header)
        # self.res_cook = self.response.cookies.get_dict()

    def isLogin(self,mail,password):
        log_resp = self.session.get(self.log_url)
        res_cook = log_resp.cookies.get_dict()
        html = etree.HTML(log_resp.text)
        auth_token = html.xpath('//div[@id="login"]/form/input[@name="authenticity_token"]/@value')[0]
        form_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': auth_token,
            'login': mail,
            'password': password
        }
        sess_resp = self.session.post(self.session_url, data=form_data,cookies=res_cook)
        # 保存cookies
        sess_cook = sess_resp.cookies.get_dict()
        res_cook.update(sess_cook)
        sess_html = etree.HTML(sess_resp.text)
        repo_resp = self.session.get(self.repo_url,cookies=res_cook)
        if repo_resp.status_code == 200:
            # print("登陆成功")
            self.is_status = True
        # return repo_resp.status_code
        return self.is_status
