#! /usr/bin/env python3
#-*- coding: utf-8 -*-
#主机字节序和网络字节序之间相互转换

#TODO
#ntol()把网络字节序转换成长整型主机字节序。 n表示网络 h表示主机 l表示长整型 s表示短整型

import socket

def convert_integer():
    data = 1234
    # 32-bit
    print("Original: %s => Long host byte order: %s, Network byte order: %s" % (data, socket.ntohl(data), socket.htonl(data)))

    # 16-bit
    print("Original: %s => Short host byte order: %s, Network byte order: %s" % (data, socket.ntohs(data), socket.htons(data)))

if __name__ == '__main__':
    convert_integer()