import os
import jinja2
from mysql import connect
import time 
template_loader = jinja2.FileSystemLoader(searchpath=os.path.dirname(os.path.abspath(__file__)))
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template("index.html")

sql  = """select name,qq,server,UNIX_TIMESTAMP(login_time) from user """
result = connect(sql,'find')
data =  []
for i in result :
    data.append({"username":i[0],"qq":i[1],"server":i[2],"login_time":time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i[3]))})
content = {'userinfo': data}

template.render(content)

# content = {'userinfo' : [
#     {'id' : 1, 'username' : 'monkey1', 'age' : 20, 'tel' : '132xx', 'address' : 'beijing', 'create_time' : '2018-09-16 12:49:14.486554', 'update_time' : '2018-09-16 12:49:14.486554'},
#     {'id' : 2, 'username' : 'monkey2', 'age' : 20, 'tel' : '132xx', 'address' : 'beijing', 'create_time' : '2018-09-16 12:49:14.486554', 'update_time' : '2018-09-16 12:49:14.486554'},
#     ]
# }
#
html_str = template.render(content)
print(html_str)
