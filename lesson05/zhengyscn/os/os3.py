import os
import socket
import getpass


'''

[vagrant@zhengyscn os]$
[登录用户@主机名 当前目录最后一级]标识符
'''

while True:
    hostname = socket.gethostname()
    # print(hostname)

    curr_username = getpass.getuser()
    # print(curr_username)

    workdir = os.path.dirname(os.path.abspath(__file__)).split('/')[-1]
    # print(workdir)

    uid = os.getuid()
    if uid == 0:
        iden = '#'
    else:
        iden = '$'

    prompt = "\033[32m[{}@{} {}]{}\033[0m ".format(curr_username, hostname, workdir, iden)
    cmd = input(prompt)
    if cmd.startswith('rm'):
        print("Warning: ")
    else:
        os.system(cmd)