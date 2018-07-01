#! /usr/bin/env python3
#-*- coding: utf-8 -*-
#设定并获取默认的套接字超时时间

#TODO
#s.gettimeout() 获取超时时间秒 none表示禁用了超时检查
#s.settimeout() 设置超时时间

#地址族
#socket.AF_INET IPv4 默认
#socket.AF_INET6 IPv6

#类型
#socket.SOCK_STREAM 流式socket for TCP （默认）
#socket.SOCK_DGRAM 数据报式socket for UDP

import socket

def test_socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Default socket timeout: %s" % (s.gettimeout()))
    s.settimeout(10)
    print("Current socket timeout: %s" % (s.gettimeout()))

if __name__ == "__main__":
    test_socket_timeout()