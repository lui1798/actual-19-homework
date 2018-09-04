## lesson05
> 我已经把上课的笔记上传到zhengyscn目录下了，方便大家复习；

- 熟悉logging模块， 能在lesson4作业中用到此模块；

```bash
import logging

logging.basicConfig(level=logging.DEBUG,
                format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                filename='/var/log/mgt.log',
                filemode='a'
                )
                
                
# Usage
logging.debug('User is lock!!!')
logging.info('login sucess.')
logging.war('file not found.')
logging.critical('mem oom')


提示：
1. 登录时需要记录日志， 登录成功 可以用debug日志级别，登录失败 可以用warn日志级别；
2. 增加用户 记录增加用户的及增加用户的参数 日志可以用debug
3. 删除用户 记录删除用户的及删除用户的参数 日志可以用debug
4. 修改用户 记录修改用户的及修改用户的参数 日志可以用debug
如果增加用户、删除用户、修改用户错误，可以用warn日志级别；

查找及分页可以不用记录日志；
```

## 整理上课的知识点， 课下做好笔记；

- json | pickle
- os
- sys
- (__name__) 和 (__file__)
- 集合
- 函数
- 装饰器
