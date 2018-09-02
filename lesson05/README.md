## lesson05

> homework

```bash
import logging

logging.basicConfig(level=logging.DEBUG,
                format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                filename='/var/log/agent.log',
                filemode='a'
                )
                
                
# Usage
logger.debug("")
logger.info("")

```
