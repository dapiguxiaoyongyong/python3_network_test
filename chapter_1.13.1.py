#! /usr/bin/env python3
#-*- coding: utf-8 -*-
#编写一个SNTP客户端

#TODO
#学到一个知识点
#建立socket.SOCK_STREAM（TCP） 发送时候socke要调用connet函数
#socket.SOCK_DGRAM（UDP） 不用

import socket
import struct
import sys
import time

NTP_SERVER = '0.uk.pool.ntp.org'
NTP_SERVER = 'cn.ntp.org.cn'
TIME1970 = 2208988800

def sntp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    server_address = (NTP_SERVER, 123)
    #client.connect(server_address)
    data = '\x1b' + 47 * '\0'
    client.sendto(data.encode(), server_address)
    
    data, address = client.recvfrom(1024)
    if data:
        print('Response received from:', address)
    t = struct.unpack('!12I', data)[10]
    t -= TIME1970
    print('\tTime=%s' % time.ctime(t))

if __name__ == '__main__':
    sntp_client()