#!/usr/bin/env python
# coding:utf-8

import socket

s = socket.socket()
s.bind(('0.0.0.0', 8888))

s.listen(5)

print "sever starting"
conn, addr = s.accept()

msg = conn.recv(1024).decode('utf-8')

print msg

conn.close()
s.close()





























