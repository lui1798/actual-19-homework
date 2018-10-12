### github账号的token：
 - 218f44a13dd981c96ef3dcbedc6fa576a067039c
### 功能：
    对用户信息列表进行增、删、改、查、保存至excel文件、退出操作
    将用户数据渲染到网页
    操作账号出错锁定
 - 增：追加新用户
 - 删：对指定的用户ID记录进行删除
 - 改：对指定的用户ID记录进行修改
 - 查：根据ID查找指定用户、查找所有用户
 - 存：将用户信息保存至数据库中或excel文件
 - 渲染：将用户数据返回到网页
 - 锁：错误超三次将按设定的时长进行锁定，保存到锁定文件lock中
### 建库建表
    CREATE DATABASE user_sys;
    CREATE TABLE auth_user(
        id int PRIMARY KEY AUTO_INCREMENT,
        username varchar(30),
        age int(3),
        tel varchar(30),
        address varchar(50),
        create_time datetime(6),
        update_time datetime(6)
    );

### 文件结构说明：
![](dir.png)