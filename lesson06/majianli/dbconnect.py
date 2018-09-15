import pymysql
def conn_db(kkk):
    db = pymysql.connect('127.0.0.1','root','123456','user')
    cursor = db.cursor()
    sql = kkk
    if sql.startswith('select'):
        cursor.execute(sql)
        data = cursor.fetchall()
        return data
    elif sql.startswith('insert'):
        try:
            cursor.execute(sql)
            db.commit()
            print('用户写入成功')
        except Exception as e:
            db.rollback()
            print('用户写入失败：原因：{}'.format(e))
    elif sql.startswith('delete'):
        try:
            cursor.execute(sql)
            db.commit()
            print('用户删除成功')
        except Exception as e:
            db.rollback()
            print('用户删除失败：原因：{}'.format(e))
    elif sql.startswith('update'):
        try:
            cursor.execute(sql)
            db.commit()
            print('用户跟新成功')
        except Exception as e:
            db.rollback()
            print('用户跟新失败：原因：{}'.format(e))
    db.close()

