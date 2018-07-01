#！/usr/bin//env python3
#-*- coding: utf-8 -*-
#Python Network Programming Cookbook -- Chapter -1
#This program is optimized forr Python 3.7. It may run on any other Python version with/without modifications.
#获取设备名和IPv4地址

import socket

def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print("Host name: %s", host_name)
    print("IP address: %s", ip_address)

if __name__ == '__main__':
    print_machine_info()