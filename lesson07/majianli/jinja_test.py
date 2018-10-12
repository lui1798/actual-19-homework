import pymysql.cursors
from jinja2 import Environment, PackageLoader

def conn_db(kkk):
    db = pymysql.connect('127.0.0.1','root','123456','user', cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = kkk
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def jinja1():
    try:
        res = conn_db('select * from user_list;')
        env = Environment(loader=PackageLoader('result'))
        template = env.get_template('jinja_html.html')
        content = template.render( items = res )

        f = open("user.html", "w")
        f.write(content)
        f.close()
        print('导出HTML成功')
    except Exception as e:
        print(e)

