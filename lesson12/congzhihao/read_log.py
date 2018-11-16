import os
import time

KEYWORD = 'WARNING'
SLEEP_TIME = 60

def log_analysis(key):
    path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(path,'django.log')
    num = 0
    # print(file_path)
    with open(file_path,'r') as f:
        line = f.readline()
        while line:
            if KEYWORD in line:
                num += 1
            line = f.readline()
        return num

def main():
    while True:
        print('{} 出现 {} 次'.format(KEYWORD,log_analysis(KEYWORD)))
        time.sleep(SLEEP_TIME)

if __name__ == '__main__':
    main()