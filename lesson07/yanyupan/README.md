### github账号的token：
 - 218f44a13dd981c96ef3dcbedc6fa576a067039c
### 功能：
> 对用户信息列表进行增、删、改、查、保存至excel文件、退出操作
> 将用户数据渲染到网页
> 操作账号出错锁定
 - 增：追加新用户
 - 删：对指定的用户ID记录进行删除
 - 改：对指定的用户ID记录进行修改
 - 查：根据ID查找指定用户、查找所有用户
 - 存：将用户信息保存至数据库中或excel文件
 - 渲染：将用户数据返回到网页
 - 锁：用户输入错误超三次将按设定的时长进行锁定，保存到锁定文件lock中

### 文件结构说明：

├── apps
│   ├── __init__.py
│   ├── login.py		github账号登陆、token认证、账号出错锁定等函数
│   ├── oper.py			登陆后操作
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── login.cpython-36.pyc
│   │   └── oper.cpython-36.pyc
│   └── utils
│       ├── date.py		日期相关函数
│       ├── db.py		数据库操作函数
│       ├── file.py		读文件、写文件、写execl文件等函数
│       ├── fmt.py		显示函数
│       ├── http.py		url请求返回相关函数
│       ├── __init__.py
│       ├── log.py		写入日志函数
│       ├── msg.py		操作成功、失败显示信息函数、提示输入信息函数
│       └── __pycache__
├── auth_render
│   ├── css
│   │   └── list.css
│   ├── index.html		渲染页面
│   ├── js
│   └── render.py		渲染函数
├── conf.ini			配置文件
├── lock			锁信息文件
├── main.py			主函数
├── operate.log			操作日志
└── user_sys.xls		保存后的excel文件
