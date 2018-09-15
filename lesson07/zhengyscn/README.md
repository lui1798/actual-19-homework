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

