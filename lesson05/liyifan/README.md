# admin_sys_v4



### 新增：logging日志记录
* 登录成功记录/失败记录

<img width="500"  src="https://github.com/1LiMingming1/readme_add_pic/blob/master/1.png">

* 操作记录/信息修改记录
 ![Image text](https://github.com/1LiMingming1/readme_add_pic/blob/master/2.png)   


### 登录账号密码
账号：admin<br/>密码：123456



### 实现功能
#### 登录
账号密码错误三次，系统锁定20秒，20秒后解锁



#### 持久化
将系统处理完成的信息写入文本



#### 操作
* add操作：增加用户信息
* delete操作：删除信息，并将在删除序号之后的所有信息的id都-1，从而使得id号保持连贯
* modify操作：更新修改信息
* list_find操作：查询符合搜索关键词的信息，做分页处理，每页2条信息
* list_all操作：显示所有信息
* save操作：将操作保存
* exit操作：输入y保存并退出，输入n不保存退出，输入其他取消退出操作，返回系统

