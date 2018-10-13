
import os

print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(__file__))


import jinja2


template_loader = jinja2.FileSystemLoader(searchpath=os.path.dirname(os.path.abspath(__file__)))
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template("templates/users.html")

