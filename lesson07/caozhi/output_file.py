import json
import time
import datetime
import os
import xlwt,xlrd
import jinja2
import prettytable
import output_log


def output_csv(user_select):
    data = xlwt.Workbook(encoding='utf-8')
    table = data.add_sheet('Sheet 1', cell_overwrite_ok=True)
    keys = ["uid", "name", "age", "tel", "address", "createTime", "create_time", "updateTime", "update_time"]
    for x in range(len(keys)):
        table.write(0, x, keys[x])
    for i in range(len(user_select)):
        for j in range(len(user_select[i])):
            table.write(i+1, j, user_select[i][j])
    data.save('new.csv')
    print('成功导出csv 文件, new.csv')
    output_log.log_log('warn','成功导出csv 文件, new.csv')

def output_html(user_select):
    template_loader = jinja2.FileSystemLoader(searchpath=os.path.dirname(os.path.abspath(__file__)))
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("index.html")
    content = {'user_select': user_select
    }
    html_str = template.render(content)
    with open('new.html', 'w') as fd:
        fd.write(html_str)
    print('成功导出html 文件, new.html')
    output_log.log_log('warn','成功导出html 文件, new.html')

def dont_output():
    print('再见~')

def illegal():
    print("输入非法，再见")
