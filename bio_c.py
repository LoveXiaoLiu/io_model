#!/usr/bin/env python
# coding:utf-8

import socket

s = socket.socket()

s.connect(('127.0.0.1', 8888))

print "clint starting"

s.send(u'正在发送数据'.encode('utf-8'))

s.close()





























