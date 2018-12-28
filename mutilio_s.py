#!/usr/bin/env python
# coding:utf-8

from socket import *
import select

s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',8888))
s.listen(5)
s.setblocking(True) #设置socket的接口为非阻塞
read_l=[s,] # 数据可读通道的列表
while True:
    # 监听的read_l中的socket对象内部如果有变化，那么这个对象就会在r_l
    # 第二个参数里有什么对象，w_l中就有什么对象
    # 第三个参数 如果这里的对象内部出错，那会把这些对象加到x_l中
    # 1 是超时时间
    r_l,w_l,x_l=select.select(read_l,[],[],1)
    print(r_l)
    for ready_obj in r_l:
        if ready_obj == s:
            conn,addr=ready_obj.accept() #此时的ready_obj等于s
            read_l.append(conn)
        else:
            try:
                data=ready_obj.recv(1024) #此时的ready_obj等于conn
                if not data:
                    ready_obj.close()
                    read_l.remove(ready_obj)
                    raise Exception('连接断开')
                ready_obj.send(data.upper())
            except:
                ready_obj.close()
                read_l.remove(ready_obj)































