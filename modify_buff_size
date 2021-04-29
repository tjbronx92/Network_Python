#!/usr/bin/env python3

import socket

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modify_buff_size():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    ''' manipulate socket options (SOL=socket option level)
    SO_SNDBUF - Send Buffer fills if remote side is not reading.
    Kernel stops sending data when send buffer is full.'''
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Buffer size [Before]: ", bufsize)
    
    ''' socket option level = TCP
    socket option = bypass Nagle Delays and send the data immediately
    sizeof(int)) = length of option value''' 
    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)

    sock.setsockopt(socket.SOL.SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)

    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Buffer size [After]: ", bufsize)

if __name__ == "__main__"
    modify_buff_size()
