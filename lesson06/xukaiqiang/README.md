## Install
  - 安装mysql
  - 导入createtable.sql
  - 修改db_config.json  mysql配置信息
  - pip install -r requirements.txt 安装python依赖模块
## userdemo

此项目是python构建的管理员演示系统,具有一下功能:

 - github账户登陆验证
 - 添加用户信息
 - 修改用户信息
 - 删除用户信息
 - 保存用户信息(保存excel)
 - 退出登陆
 - 本项目中对pymyslq进行简单封装,具有增删改查多条删除,多条更改插入功能
 - 登陆github模块使用xpath进行处理html标签

## 用户数据类型 

### 登陆

- github用户名密码

### 数据实例:

```
users = [
    {'name' : 'monkey1', 'age':20, 'tel':'132xxx', 'address':'beijing', 'id':1},
    {'name' : 'monkey2', 'age':20, 'tel':'132xxx', 'address':'beijing', 'id':2},
    {'name' : 'monkey3', 'age':20, 'tel':'132xxx', 'address':'beijing', 'id':3},
]

```

## 项目运行

```
git clone https://github.com/xxxxx/usersysdemo.git

python usersysdemo.py

```

## 效果演示

- github用户登陆

	![login](https://raw.githubusercontent.com/iteemo/images/master/lesson06/githubdenglu.png)

- 添加用户

	![adduser](https://raw.githubusercontent.com/iteemo/images/master/lesson04/adduser.png)


- 删除用户

	![adduser](https://raw.githubusercontent.com/iteemo/images/master/lesson04/del.png)

- 保存用户

	![adduser](https://raw.githubusercontent.com/iteemo/images/master/lesson04/save.png)

- 锁定用户

	![adduser](https://raw.githubusercontent.com/iteemo/images/master/lesson04/lock.png)