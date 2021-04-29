#!/usr/bin/env python3

import socket

def test_socket_timeout():
    #Create socket(IPv4,TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Default socket timeout: {}".format(s.gettimeout()))
    #timeout on blocking socket operation in seconds
    s.settimeout(100)
    print("Current socket timeout: {}".format(s.gettimeout()))

if __name__ == '__main__':
    test_socket_timeout()
