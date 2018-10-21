import socket



sk = socket.socket()
sk.bind(('0.0.0.0', 9991))
sk.listen(5)

while True:
    print('Start Server ...')
    print("Listen 9999")
    # 等待链接,阻塞，直到渠道链接 conn打开一个新的对象专门给当前链接的客户端 addr是ip地址
    conn, addr = sk.accept()
    print("client addr:",str(addr))
    while True:
        recvData = conn.recv(1024)
        recvData = '''
        HTTP/1.1 200 OK
Server: JSP3/2.0.6
Date: Wed, 04 Feb 2015 08:19:53 GMT
Content-Type: image/gif
Content-Length: 43
Connection: keep-alive
Last-Modified: Mon, 28 Jul 2014 03:15:11 GMT
Expires: Wed, 04 Feb 2015 08:22:23 GMT
Age: 447
Cache-Control: max-age=600
Accept-Ranges: bytes
Timing-Allow-Origin: http://www.baidu.com
        '''
        conn.send(bytes(recvData.decode("utf-8"),"utf-8"))
    conn.close()