用户信息管理系统<br>
__author__ = caozhi<br>
最后更新时间 2018-10-13<br>
__version__ = 5.1<br>

—— 管理员账号密码：测试token账号：5775cbe26a3a3b153a3be6e68b9925e8db10557e<br>
—— 密码进行密文输入<br>

用户信息存储格式：<br>
—— 对数据进行存储到数据库，方便以后读取 库：USERMESSAGE，表：message<br>
—— 数据库账号和密码 已用base64加密 存到配置文件里<br>

可以实现以下功能：<br>
 1、账户30s 内只能登陆失败3次，超过失败次数则锁定(锁定时间可自定义调整配置文件)，需要30s 后再次登录重试<br>
 2、对用户信息的增删改查操作。查看可以分页展示，并导出csv文件和html文件 功能<br>
 3、打印追加日志到当前目录 error.log 里，并按天切割<br>
 增：追加新用户信息<br>
 删：对指定id记录进行删除<br>
 改：对指定id记录进行更新<br>
 查：根据输入的字符串 模糊查找 id name tel address，结果并分页展示，并可以导出csv文件和html文件 功能<br>

运行main.py，具体自测结果见test.....<br>

文件函数说明：<br>

├── main.py			主函数<br>
├── conf.ini			统一配置文件<br>
├── dbmysql.py			数据库操作函数<br>
├── error.log.2018-10-13	日志信息(按天切割)<br>
├── index.html			导出html模板<br>
├── login_def.py		登陆/锁定 函数<br>
├── new.csv			导出csv样版<br>
├── new.html			导出html样版<br>
├── operate.py			用户操作相关函数<br>
├── output_file.py		导出csv和html 函数<br>
├── output_log.py		日志处理函数<br>
├── README.md			说明<br>
└── test			自测结果<br>


附件：
show create table  message;

CREATE TABLE message(
uid INT NOT NULL AUTO_INCREMENT,
name VARCHAR(20) NOT NULL,
age VARCHAR(10) NOT NULL,
tel VARCHAR(40) NOT NULL,
address VARCHAR(60) NOT NULL,
createTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
create_time int(10) NOT NULL DEFAULT '0',
updateTime TIMESTAMP  DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
update_time int(10) NOT NULL DEFAULT '0',
PRIMARY KEY ( uid )    
)DEFAULT CHARSET=utf8;
