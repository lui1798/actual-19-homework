import logging

LOG_LEVEL = logging.DEBUG
LOG_FORMAT = '[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s'
LOG_FILENAME = 'usermanage.log'
LOG_FILEMODE = 'a'
LOG_ENCODING = 'utf-8'

logger = logging.getLogger('log')
logger.setLevel(LOG_LEVEL)
fh = logging.FileHandler(LOG_FILENAME, encoding=LOG_ENCODING)
fh.setLevel(LOG_LEVEL)
fh.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(fh)


# 装修器函数，显示操作提示的同时将操作日志保存到日志文件
def Log_Msg(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "debug":
                logger.debug(*args, **kwargs)
            elif level == "warn":
                logger.warn(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator