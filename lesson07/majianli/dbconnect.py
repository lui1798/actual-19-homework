# import pymysql.cursors
import pymysql.cursors
def conn_db(kkk):
    # db = pymysql.connect('127.0.0.1','root','123456','user', cursorclass=pymysql.cursors.DictCursor)
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
            if cursor.rowcount >= 1:
                print('成功写入{}条数据'.format(cursor.rowcount))
        except Exception as e:
            db.rollback()
            print('用户写入失败：原因：{}'.format(e))
    elif sql.startswith('delete'):
        try:
            cursor.execute(sql)
            db.commit()
            if cursor.rowcount >= 1:
                print('用户删除成功,共删除{} 条'.format(cursor.rowcount))
        except Exception as e:
            db.rollback()
            print('用户删除失败：原因：{}'.format(e))
    elif sql.startswith('update'):
        try:
            cursor.execute(sql)
            db.commit()
            if cursor.rowcount >= 1:
                print('用户跟新成功,共更新{} 条'.format(cursor.rowcount))
        except Exception as e:
            db.rollback()
            print('用户跟新失败：原因：{}'.format(e))
    db.close()

