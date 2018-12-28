#!/usr/bin/env python
# coding:utf-8

from socket import *

from io import BlockingIOError
import time
s=socket(AF_INET,SOCK_STREAM)
s.bind(('127.0.0.1',8888))
s.listen(5)
s.setblocking(True) #设置socket的接口为非阻塞
conn_l=[] # 存储和server的连接 的 连接
del_l=[] # 存储和和server的断开 的 连接
while True:
    try:
        # 这个过程是不阻塞的
        conn,addr=s.accept() # 当没人连接的时候会报错，走exception（<- py中是except）
        conn_l.append(conn)
    except:
        print(conn_l)
        for conn in conn_l:
            try:
                data=conn.recv(1024)
                if not data:
                    del_l.append(conn)
                # 这个过程是不阻塞的
                data=conn.recv(1024) # 不阻塞
                if not data: # 如果拿不到data
                    del_l.append(conn) # 在废弃列表中添加conn
                    continue
                conn.send(data.upper())
            except:
                del_l.append(conn)

        for conn in del_l:
            conn_l.remove(conn)
            conn.close()
        del_l=[]






























