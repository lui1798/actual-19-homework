#encoding:utf-8
import os
import time
#import pyinotify

pos = 0

def printlog(logfile):
    global pos
    LOGLEVEL = ['[DEBUG]', '[INFO]', '[WARNING]', '[ERROR]']
    debug_num = 0
    info_num = 0
    warn_num = 0
    error_num = 0
    try:
        fhandle = open(logfile)
        if pos != 0:
            fhandle.seek(pos,0)
        while True:
            line = fhandle.readline()
            print(line)
            if line != '':
                cell = line.strip().split()
                if len(cell) > 3 and cell[3] in LOGLEVEL:
                    if cell[3] == '[DEBUG]':
                        debug_num += 1
                    elif cell[3] == '[INFO]':
                        info_num += 1
                    elif cell[3] == '[WARNING]':
                        warn_num += 1
                    elif cell[3] == '[ERROR]':
                        error_num += 1
            pos = pos + len(line)
            if line == '':
                break
        fhandle.close()
        print('debug_num:{0},info_num:{1},warn_num:{2},error_num:{3},pos:{4}'.format(debug_num, info_num, warn_num, error_num, pos))

    except Exception as e:
        print(str(e))


def log_stat(path):
    path = path
    filename = 'django.log'
    logfile = os.path.join(path,filename)

    while True:
        printlog(logfile)
        print('-----------')
        time.sleep(60)


if __name__ == "__main__":
    path = '/home/luxx/documents/reboot19/webapp/logs/'
    log_stat(path)














'''
class OnWriteHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print("create file: {0} ".format(os.path.join(event.path,event.name)))

    def process_IN_MODIFY(self, event):
        if event.name == 'django.log':
            logfile = os.path.join(event.path,event.name)
            try:
                printlog(logfile)
            except Exception as e:
                raise e
            print("modify file: {0} ".format(os.path.join(event.path,event.name)) )


def auto_compile(path):
        wm = pyinotify.WatchManager()
        mask = pyinotify.IN_CREATE | pyinotify.IN_MODIFY # 还有删除等
        notifier = pyinotify.Notifier(wm, OnWriteHandler())
        wm.add_watch(path, mask, rec=True, auto_add=True)
        print('==start to watch path: {0} =='.format(path))
        while True:
            try:
                notifier.process_events()
                if notifier.check_events():
                    notifier.read_events()
            except KeyboardInterrupt:
                notifier.stop()
                break

if __name__ == "__main__":
    path = '/home/luxx/documents/reboot19/webapp/logs/'
    auto_compile(path) #启动之后，可以到指定的目录下面创建或者修改文件，然后看shell输出信息



        elif event.name == 'server.log':
            logfile = os.path.join(event.path,event.name)
            try:
                printlog(logfile)
            except Exception as e:
                raise e
            print("modify file: {0} ".format(os.path.join(event.path,event.name)) )
'''
