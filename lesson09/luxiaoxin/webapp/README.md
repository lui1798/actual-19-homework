## 登录用户名密码
 - 账号：admin
 - 密码：51@reboot
 
## 操作说明
 - python manage.py runserver 0.0.0.0：8888启动webapp项目web服务
 - 浏览器打开url：http://192.168.137.128:8888/login/
 - 输入用户名密码，点击登录按钮，系统成功登录后自动跳转到主页(index.html文件)可进行服务器操作交互，点击退出回到登录界面
 - 选择导航栏“命令执行”菜单，按提示在文本框输入Linux命令，点击提交，当前页面呈现命令执行结果
 - 选择导航栏“数据求和”菜单，按提示在文本框输入需要计算的数字，点击求和，当前页面呈现计算结果
 
## 本周作业完成内容
 - 使用django建立webapp项目，添加两个app：api&dashboard
 - 使用form的action来触发实现“命令执行”和“数据求和”功能
 - 使用render将views.py中函数执行的结果传递到前端html页面中呈现
 
## 环境说明
 - 使用virtualenv建立python3虚拟环境python36env
 - python3.7 django1.11 MySQL8.0
