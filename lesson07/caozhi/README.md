用户信息管理系统
__author__ = caozhi
最后更新时间 2018-10-12
__version__ = 5.1

—— 管理员账号密码：测试token账号：5775cbe26a3a3b153a3be6e68b9925e8db10557e
—— 密码进行密文输入

用户信息存储格式：
—— 对数据进行存储到数据库，方便以后读取 库：USERMESSAGE，表：message
—— 数据库账号和密码 已用base64加密 存到配置文件里

可以实现以下功能：
 1、账户30s 内只能登陆失败3次，超过失败次数则锁定(锁定时间可自定义调整配置文件)，需要30s 后再次登录重试
 2、对用户信息的增删改查操作。查看可以分页展示，并导出csv文件和html文件 功能
 3、打印追加日志到当前目录 error.log 里，并按天切割
 增：追加新用户信息
 删：对指定id记录进行删除
 改：对指定id记录进行更新
 查：根据输入的字符串 模糊查找 id name tel address，结果并分页展示，并可以导出csv文件和html文件 功能

运行main.py，具体自测结果见test.....

文件函数说明：

├── conf.ini			统一配置文件
├── error.log.2018-10-12	日志信息(按天切割)
├── index.html			导出html模板
├── login_def.py		登陆/锁定 函数
├── main.py			主函数
├── new.csv			导出csv样版
├── new.html			导出html样版
├── operate.py			用户操作相关函数
├── output_log.py		日志处理函数
├── README.md			说明
└── test			自测结果

