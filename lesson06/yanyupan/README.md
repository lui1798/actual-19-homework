### 管理员账号密码：
 - 账号：admin
 - 密码：111111
 > 暂未实现以Github(Token)方式认证登录，目前以存储到配置文件中，以hash形式进行验证登陆
### 用户信息存储格式：
> 存储至数据库user_sys表user中
### 功能：
> 对用户信息列表进行增、删、改、查、保存、保存至excel文件、退出操作
 - 增：追加新用户
 - 删：对指定的用户ID记录进行删除
 - 改：对指定的用户ID记录进行修改
 - 查：根据用户输入的用户名或电话或地址进行查询，按分页查询
 - 存：将用户信息保存至数据库中或excel文件
 - 锁：用户输入错误超三次将按设定的时长进行锁定，保存到锁定文件lock中

### 文件函数说明：
 - main.py		主函数
 - lock.py		用户锁定相关函数
 - login.py		登陆函数
 - oprusers.py		用户操作相关函数
 - config.py		读取配置文件信息函数
 - conf.ini		统一配置文件
 - user_sys.xls		存储成excel格式的文件
 - usermanage.log	日志信息

 - utils/db.py		数据库操作相关函数
 - utils/file.py	文件读写、excel写入等操作函数
 - utils/hash.py	生成hash函数
 - utils/log.py		日志处理函数
 - utils/print_msg.py	信息提示相关函数
