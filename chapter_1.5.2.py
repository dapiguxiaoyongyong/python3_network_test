#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#主要使用getservbyport

#TODO
#socket.getservbyport(port,[protocolname]) 获取服务的名字 比如http smtp domain
#注意 端口不是通用端口 会报错

import socket

def find_service_name():
    protocolname = 'tcp'
    for port in [80,25]:
        print("Port: ", port, " service name: ", socket.getservbyport(port,protocolname))

    tmp_port = 53
    print("Port: ", tmp_port, " service name: ", socket.getservbyport(tmp_port))

    tmp_port = 443
    print("Port: ", tmp_port, " service name: ", socket.getservbyport(tmp_port))

if __name__ == '__main__':
    find_service_name()