## 本周作业完成内容
 - webapp项目增加logger功能，项目代码中把所有的print全部替换成logger日志，日志输出到webapp项目的logs目录下；
 - webapp项目用户models的功能全部实现，增删改查、搜索、分页、导出；
 - webapp项目增加“日志分析”功能，新增loganalysis的app，MySQL新建log统计表log，在loganalysis目录下建立management/commands/ 目录和todb.py文件，增加python manage.py todb命令，运行指令实现不同日志级别每分钟出现次数统计数据自动入库；
 - webapp项目增加“日志分析”功能，功能下的“系统日志分析”页面显示最近一次统计的日志信息，表格显示每分钟匹配的不同日志级别【'[DEBUG]', '[INFO]', '[WARNING]', '[ERROR]'】出现的次数；
 - webapp项目增加“日志分析”功能，功能下的“乘法表”页面显示99乘法表；
 - 根目录下的log_statistics.py脚本实现日志统计功能，打印每分钟匹配DEBUG，INFO，WARNING，ERROR出现的次数；
 - 根目录下的mul_table.py脚本实现打印99乘法表功能。


## 系统登录用户名密码
 - 账号：admin
 - 密码：51@reboot
 
## 系统功能操作说明
 - python manage.py runserver 0.0.0.0:8888启动webapp项目web服务
 - 浏览器打开url：http://192.168.137.128:8888/account/login/
 - 输入用户名密码点击登录按钮，系统成功登录后自动跳转到主页(index.html)进行操作交互，点击退出回到登录界面
 - 选择导航栏“资源管理-资产管理”菜单，可查看资产列表，对应界面上可以进行资产的增、删、改、查
 - 选择导航栏“用户管理-用户管理”菜单，可查看用户列表，对应界面上可以进行用户的增、删、改、查
 - 选择导航栏“日志分析-系统日志分析”菜单，可查看系统最近1分钟的不同日志级别【'[DEBUG]', '[INFO]', '[WARNING]', '[ERROR]'】出现的次数
 - 选择导航栏“日志分析-乘法表”菜单，可查看99乘法表
 

