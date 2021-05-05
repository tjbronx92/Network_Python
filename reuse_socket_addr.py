#!/usr/bin/venv python3

import SOL_SOCKET
import sys

#getsockopt() and setsockopt() manipulate options for the socket referred to by the file descriptor sockfd.  Options may exist at multiple protocol levels; they are always present at the uppermost socket level.
def reuse_socket_addr():
    #Create socket(IPv4, TCP) & assign to variable sock.
    sock = socket.socket(socket.AF_INET, socekt.SOCK_STREAM)

    #Get old state of the SO_REUSEADDR option
    #getsockopt() - the level at which the option resides and the name of the option must be specified.
    old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print("Old sock state: {}".format(old_state))

    #Enable the SO_REUSEADDR option
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
