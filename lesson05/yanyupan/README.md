### 管理员账号密码：
 - 账号：admin
 - 密码：111111
### 用户信息存储格式：
> [
>   {"id": 1, "name": "yan", "age": 88, "tel": 155555, "address": "fujian"},
>   {"id": 2, "name": "li", "age": 77, "tel": 156666, "address": "xinjiang"},
>   {"id": 4, "name": "wang", "age": 33, "tel": 18666, "address": "fujian"}
> ]
### 功能：
> 对用户信息列表进行增、删、改、查、保存、退出操作
 - 增：追加新用户
 - 删：对指定的用户ID记录进行删除
 - 改：对指定的用户ID记录进行修改
 - 查：根据用户输入的信息与用户的名字及用户的地址进行匹对查询，按分页查询
 - 存：将用户信息保存成文件user.json
 - 锁：用户输入错误超三次将按设定的时长进行锁定，保存到锁定文件lock中

### 功能与前一版差异：
 - 修改分页显示时，按q键返回上级菜单
 - 增加将相关信息收集至日志文件
### 涉及自定义函数：
 - 读文件函数：read_file(fname)
 - 写文件函数：write_file(fname, data, ser)
 - 将操作日志记录函数：log_msg(level)
 - 操作成功时提示信息函数：succ_msg(msg)
 - 操作错误或警告时提示信息函数：warn_msg(msg)
 - 提示用户输入函数：input_msg(msg)
 - 显示用户信息函数：print_users(users)
 - 锁定用户函数：lock_user()
 - 判断是否被锁定函数：is_unlock()
 - 登录函数：login()
 - 获取用户信息：get_users()
 - 增加用户信息函数：add_user(users)
 - 删除用户信息函数：del_user(users)
 - 修改用户信息函数：modify_user(users)
 - 查询用户信息函数：query_user(users)
 - 保存用户信息函数：save_users(users)
 - 选择操作函数：operate(users)
 - 主函数：main()
### 自定义函数与前一版差异：
 - 函数read_file(fname)与write_file(fname, data, ser)的文件打开方式由open改成with open方式
 - 拆分提示信息函数print_msg(msg, status)为succ_msg(msg)与warn_msg(msg) [注：为了与日志记录函数结合]
 - 新增操作日志记录函数log_msg(level)

### 遇到问题：
 - 日志记录文件乱码

### 逻辑图与上版一致，暂略