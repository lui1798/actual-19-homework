import pymysql

user_keys = ['id', 'name', 'age', 'tel', 'addr']

def connect():
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='', database='users_info', port=3306)

    except Exception as e:
        print(e)

    else:
        return conn

def Select(info = None):
    conn =  connect()
    selet_sql = 'select * from users_list;'

    cursor = conn.cursor()
    cursor.execute(selet_sql)
    a = {'id':0,'name':1,'age':2,'tel':3,'addr':4}
    b= []
    for x in cursor.fetchall():
        if info == None:
            b.append(x)
        else:
            b.append(x[a[info]])
    conn.close()
    return b

def Insert(user_info):
    conn =  connect()
    insert_sql = "insert into users_list(id, name, age, tel, addr)values({},'{}',{},'{}','{}');".format(*user_info)
    cursor = conn.cursor()
    cursor.execute(insert_sql)
    conn.commit()
    cursor.close()
    conn.close()

    return

def Update(uid,op,info):
    conn =  connect()
    update_sql = '''
    update users_list set {}='{}' where id = '{}';
    '''.format(op,info,uid)
    cursor = conn.cursor()
    cursor.execute(update_sql)
    conn.commit()
    cursor.close()
    conn.close()

    return

def Delete(uid):
    conn =  connect()
    delete_sql = "delete from users_list where id = '{}';".format(uid)
    cursor = conn.cursor()
    b = cursor.execute(delete_sql)
    conn.commit()
    cursor.close()
    conn.close()
    return b

def get_userdict():
    data = []
    users_info  = Select()

    for user_info in users_info:
        data.append(dict(zip(user_keys, user_info)))

    return data