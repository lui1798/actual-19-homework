
from config import ReadConfig

def main():
    msg, ok = ReadConfig('conf.ini', 'LOG', 'LOGFILE')
    if ok:
        print(msg)
    else:
        print("WARNING LOGFILExxx not found.")



if __name__ == '__main__':
    main()
