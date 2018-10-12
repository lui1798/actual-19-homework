一、功能：
1.全部采用数据库方式进行存储
2.采用模块的方式进行调用
二、使用
1.安装mysql
 user  | CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `passwd` varchar(40) NOT NULL,
  `qq` int(20) NOT NULL,
  `server` varchar(40) NOT NULL,
  `failed_time` int(11) DEFAULT '0',
  `login_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1 |
2.目录使用
root@ubuntu:~/actual-19-homework/lesson06# tree liuenyuan/
liuenyuan/
├── app
│   ├── config.py         配置模块
│   ├── log.py            日志模块
│   ├── lol.py            主程序
│   ├── mysql.py          数据库连接
│   └── __pycache__
│       ├── config.cpython-35.pyc
│       └── mysql.cpython-35.pyc
├── config
│   └── config.ini       配置文件
└── logs
    └── log              日志存储
注：请按照config.ini先行配置数据库及日志


