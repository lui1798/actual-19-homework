
import logging


logging.basicConfig(
    filename="/var/log/mgt.log",
    filemode='a',
    format="[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s",
    level = logging.DEBUG,
)


logging.debug("Welcome to 51reboot.")
logging.info("login sucess.")
logging.warning("file not found.")
logging.critical("mem moo")