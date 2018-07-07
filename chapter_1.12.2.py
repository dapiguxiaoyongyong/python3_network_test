#! /usr/bin/env python3
#-*- coding: utf-8 -*-
#从网络时间服务器获取并打印当前时间

#TODO
#在window系统下面在命令行安装 pip install ntplib


import ntplib

from time import ctime

def print_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org')
    print(ctime(response.tx_time))

if __name__ == '__main__':
    print_time()