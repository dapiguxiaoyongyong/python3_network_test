#! /usr/bin/env python3
#-*- coding: utf-8 -*-
#优雅地处理套接字错误

#TODO 注意 python 2.7 和 python 3 的socket模块里面参数有些变化
#本例子里面的 sendall recv函数就出现了问题
#In python 3, bytes strings and unicodestrings are now two different types
#参考网页内容 https://blog.csdn.net/chuanchuan608/article/details/17915959

#本py在virsual studio code用python插件调用 要传入参数 参考
#https://blog.csdn.net/u013600225/article/details/52971528
#主要是launch.json里面加入"stopOnEntry" : true 和 "args": ["--port=80","--host=www.baidu.com","--file=chapter_1.8.1.py"]



import sys
import socket
import argparse

def main():
    #setup argument parsing
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument('--host', action="store", dest="host", required=False)
    parser.add_argument('--port', action="store", dest="port", type=int, required=False)
    parser.add_argument('--file', action="store", dest="file", required=False)

    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file

    print("host %s port %d filename %s" % (host, port, filename))

    # First tyr-except block -- create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Error creating socket: %s", e)
        sys.exit(1)

    # Second try-except block -- connet to given host/port
    try:
        s.connect((host,port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        sys.exit(1)
    except socket.error as e:
        print("Connection error: %s" % e)
        sys.exit(1)

    # Third try-except block -- sending data
    try:
        #msg = bytes("GET %s HTTP/1.0\r\n\r\n" % filename,encoding='utf-8') #TODO
        msg = "GET %s HTTP/1.0\r\n\r\n" % filename
        s.sendall(msg.encode()) #TODO encode()
    except socket.error as e:
        print("Error sending data: %s" % e)
        sys.exit(1)

    while 1:
        # Fourth try-except block -- waiting to receive data from remote host
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print("Error receiving data: %s" % e)
            sys.exit(1)

        if not len(buf):
            break

        #write the received data
        sys.stdout.write(buf.decode()) #TODO decode

if __name__ == '__main__':
    main()