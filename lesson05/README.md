## lesson05
> 我已经把上课的笔记上传到zhengyscn目录下了，方便大家复习；

- 熟悉logging模块， 能用lesson4作业中用到此模块；

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
logging.warning('file not found.')
logging.critical('mem oom')

```

## 整理上课的知识点， 课下做好笔记；

- json | pickle
- os
- sys
- __name__ 和 __file__
- 集合
- 函数
- 装饰器
