## 功能
- 文本框中输入命令，返回命令执行结果
- 在表单中输入两个数，返回两数之和
## 说明：
- 命令执行采用ajax的get请求
- 两数之和采用form的action来触发
## 运行环境注意事项：
```
1. 用户python3.6版本，请安装django1.11版本
   pip install -r requirements.txt或pip install django==1.11
2. 目前采用sqlite3，如果有错误提示,请安装sqlite-devel，再重新编译安装python
3. 请将templates/command.html下script中的ip、端口(http://192.168.100.100:8000)更换成自已项目运行的ip及端口
```