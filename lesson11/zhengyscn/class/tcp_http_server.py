#!/usr/bin/env python
# coding:utf-8
import socket


response = '''HTTP/1.1 200 OK
Accept-Ranges: bytes
Cache-Control: no-cache
Connection: Keep-Alive
Content-Length: 14615
Content-Type: text/html
Date: Sun, 04 Nov 2018 02:05:33 GMT
Etag: "5bd7d86c-3917"
Last-Modified: Tue, 30 Oct 2018 04:05:00 GMT
P3p: CP=" OTI DSP COR IVA OUR IND COM "
Pragma: no-cache
Server: BWS/1.1
Set-Cookie: BAIDUID=ED2CA7E103AEB9BB83B2BC290406271C:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
Set-Cookie: BIDUPSID=ED2CA7E103AEB9BB83B2BC290406271C; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
Set-Cookie: PSTM=1541297133; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
Vary: Accept-Encoding
X-Ua-Compatible: IE=Edge,chrome=1
'''

def handle_request(client):
    buf = client.recv(1024)
    # client.send("HTTP/1.1 200 OK\r\n\r\n".encode())
    client.send(response.encode())
    client.send("Hello, World".encode())


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 9000))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()


if __name__ == '__main__':
    main()