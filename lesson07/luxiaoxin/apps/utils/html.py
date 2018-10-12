#encoding:utf-8
#-----导入内置模块--------
#-----导入开源模块--------
import os
import jinja2
#-----导入自定义模块--------
from apps.utils import db
from apps.utils.writefile import WriteFile

#--------定义功能函数-------
def WriteHtml():
    title = ('id', 'name', 'age', 'tel', 'address')
    template_loader = jinja2.FileSystemLoader(searchpath='./export/template/')
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("index.html")

    cnt, result = db.Select()
    res = [dict(zip(title, user))for user in result]

    content = {'users': res}
    template.render(content)

    html_str = template.render(content)
    print(html_str)

    WriteFile('./export/userlist.html', html_str)
