#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#将IPv4地址转换成不同的格式
#主要使用inet_aton()和inet_ntoa()

#TODO 
#binascii模块 2进制数据和ascii的转换模块
#inet_aton()返回ip地址的2进制形式
#inet_ntoa()转换2进制的ip地址到普通ip地址形式
#hexlify返回2进制数据的16进制表示

import socket
from binascii import hexlify

def convert_ip4_address():
    for ip_addr in ['127.0.0.1','192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print("IP Address:", ip_addr, "Packed:", hexlify(packed_ip_addr),"Unpacked:",unpacked_ip_addr)

if __name__ == '__main__':
    convert_ip4_address()
