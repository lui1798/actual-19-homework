import time
import threading

import logging

logging.basicConfig(level=logging.DEBUG,
                format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                             )


def f1():
    time.sleep(10)
    print("f1 finish")


def f2():
    print("f2")


threads = []
th1 = threading.Thread(target=f1, name="f1 thread")
logging.debug(th1)
th1.start()  # 创建一个县城
threads.append(th1)

th2 = threading.Thread(target=f2, name="f2 thread")
logging.debug(th2)
th2.start()
threads.append(th2)

th3 = threading.Thread(target=f1, name="f3 thread")
logging.debug(th3)
th3.start()
threads.append(th3)

th4 = threading.Thread(target=f2, name="f4 thread")
logging.debug(th4)
th4.start()
threads.append(th4)

for th in threads:
    logging.debug(th)
    th.join()  # 阻塞 直到所有线程执行完成


time.sleep(10)

print("all threads finish.")