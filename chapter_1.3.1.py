#！/usr/bin/env python3
#Python Newwork Programming Cookbook -- Chapter -1
#This program is optimized for Python 3.7
#It may run on any other version with/without modifications.

import socket

def get_remote_machine_info():
    remote_host = 'www.baidu.com'
    try:
        print("Ip address: ", socket.gethostbyname(remote_host))
    except socket.error as err_msg:
        print(remote_host,err_msg)

if __name__ == '__main__':
    get_remote_machine_info()