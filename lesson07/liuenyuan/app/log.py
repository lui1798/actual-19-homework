import logging
from config import readconfig
logfile = readconfig('log')
filename = logfile['logfile']
logging.basicConfig(format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                filename=filename,level=logging.DEBUG,
                filemode='a')
