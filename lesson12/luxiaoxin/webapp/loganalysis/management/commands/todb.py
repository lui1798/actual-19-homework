import os
import json
import time
#import pyinotify

from loganalysis.models import Log
from datetime import datetime
from django.conf import settings
from django.core.management import BaseCommand


pos = 0
LOGNAME = 'django.log'

class Command(BaseCommand):
    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, 'logs')
        logfile = os.path.join(path, LOGNAME)
        while True:
            logdata = self.analysislog(logfile)
            self.parse(logdata)
            time.sleep(60)


    def analysislog(self, logfile):
        global pos
        LOGLEVEL = ['[DEBUG]', '[INFO]', '[WARNING]', '[ERROR]']
        debug_num = 0
        info_num = 0
        warn_num = 0
        error_num = 0
        data = {}
        try:
            fhandle = open(logfile)
            if pos != 0:
                fhandle.seek(pos,0)
            while True:
                line = fhandle.readline()
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
            data['DEBUG'] = debug_num
            data['INFO'] = info_num
            data['WARNING'] = warn_num
            data['ERROR'] = error_num

            return data
        except Exception as e:
            print(str(e))




    def parse(self, data):
        for k,v in data.items():
            log = Log()
            log.logname = LOGNAME
            log.loglevel = k
            log.count = v
            log.save()

        print('parse over!')
