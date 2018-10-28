import socket



sk = socket.socket()
sk.bind(('0.0.0.0', 9000))
sk.listen(5)

# while True:
#     print('Start Server ...')
#     print("Listen 9000")
#     conn, addr = sk.accept()
#     print("client addr:",str(addr))
#     while True:
#         recvStr = conn.recv(1024)
#         respData = '''
#         HTTP/1.1 200 OK
#         Date: Sat, 29 Jul 2017 06:18:23 GMT
#         Content-Type: text/html
#         Content-Length: %d
#         Connection: Close
#         Server: reboot
#         '''.format(len(recvStr))
#         print(recvStr)
#         conn.send(bytes(respData, 'utf-8'))
#         conn.send(recvStr)
#     conn.close()


print('Start Server ...')
print("Listen 9000")
conn, addr = sk.accept()
print("client addr:",str(addr))
recvStr = conn.recv(1024)
respData = '''
HTTP/1.1 200 OK
Date: Sat, 29 Jul 2017 06:18:23 GMT
Content-Type: text/html
Content-Length: %d
Connection: Close
Server: reboot
'''.format(len(recvStr))
print(recvStr)
conn.send(bytes(respData, 'utf-8'))
conn.send(recvStr)
conn.close()