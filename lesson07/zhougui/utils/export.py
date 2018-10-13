#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @File  : exportHtml.py
# @Author: ZhouGui
# @Date  : 2018/10/13
# @Description : 导出excel文件与html文件
import os
import xlwt
import jinja2
from utils.db import list_user


def exportExcel(filename):
    users = list_user()
    wordbook = xlwt.Workbook(encoding='utf-8')
    booksheet = wordbook.add_sheet('Sheet1', cell_overwrite_ok=True)
    keys = ['id', 'name', 'age', 'tel', 'address']
    for x in range(len(keys)):
        booksheet.write(0, x, keys[x])
    for i in range(len(users)):
        for j in range(len(users[i])):
            booksheet.write(i + 1, j, users[i][keys[j]])
    wordbook.save(filename)
    print('Export users is Success')


def exportHtml():
    template_loader = jinja2.FileSystemLoader(searchpath=os.path.dirname(os.path.abspath(__file__)))
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template('user_template.html')
    content = {'userinfo': list_user()}
    html_str = template.render(content)
    with open('user.html', 'w') as fd:
        fd.write(html_str)
        print('Export users is Success')
