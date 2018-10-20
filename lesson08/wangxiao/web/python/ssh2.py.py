#coding: utf-8

import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.load_system_host_keys()
client.connect(SERVER_HOSTNAME, port=SERVER_PORT, username=SERVER_USERNAME, password=SERVER_PASSWORD)
_,stdout,_ = client.exec_command("ls -lh --color", 10240)
outputLines = stdout.readlines()
outputLines = "".join(outputLines)
print outputLines
client.close()

