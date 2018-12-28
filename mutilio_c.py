#!/usr/bin/env python
# coding:utf-8

from socket import *
c=socket(AF_INET,SOCK_STREAM)
c.connect(('127.0.0.1',8888))

for i in range(10):
    msg=str(i)
    if not msg:continue
    c.send(msg.encode('utf-8'))
    data=c.recv(1024)
    print(data.decode('utf-8'))































