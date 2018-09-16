import os
import jinja2

template_loader = jinja2.FileSystemLoader(searchpath=os.path.dirname(os.path.abspath(__file__)))
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template("index.html")

content = {'userinfo' : [
    {'id' : 1, 'username' : 'monkey1', 'age' : 20, 'tel' : '132xx', 'address' : 'beijing', 'create_time' : '2018-09-16 12:49:14.486554', 'update_time' : '2018-09-16 12:49:14.486554'},
    {'id' : 2, 'username' : 'monkey2', 'age' : 20, 'tel' : '132xx', 'address' : 'beijing', 'create_time' : '2018-09-16 12:49:14.486554', 'update_time' : '2018-09-16 12:49:14.486554'},
    ]
}

html_str = template.render(content)
print(html_str)