## lesson05

> homework

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
