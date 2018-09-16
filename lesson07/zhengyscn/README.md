## MySQL


- 创建数据库
```
CREATE DATABASE python19;
```

- 创建表
```
CREATE TABLE auth_user(
    id int PRIMARY KEY AUTO_INCREMENT,
    username varchar(30),
    age int(3),
    tel varchar(30),
    address varchar(50),
    create_time datetime(6),
    update_time datetime(6)
);
```

- 建立数据库连接

```python
conn = pymysql.connect('127.0.0.1', 'root', '123456', 'python19', 3306)
```

- 创建游标
```python
cursor = conn.cursor()


# 生成器
cursor_gen = conn.cursor(pymysql.cursors.SSCursor)
cursor_gen.fetchall_unbuffered()
```

- 增、删、改、查
```python
cursor.execute(sql)

# 查询所有结果集
cursor.fetchall()

# 查询单条数据
cursor.fetchone()

# 查询几行
cursor.fetchmany(rows=2)
```

- 提交
```python
cursor.commit()

conn.autocommit(True)
```

- 关闭
```python
cursor.close()
conn.close()
```