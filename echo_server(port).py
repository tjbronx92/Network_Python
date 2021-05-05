#!/usr/bin/#!/usr/bin/env python3

import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5

def echo_server(port):
    #Create TCP socket
    sock.socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Enable address/port reuse
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #Bind socket to port
    server_address = (host, port)
    print("Starting up echo server on {} port {}".format(server_address))
    sock.bind(server_address)
    #Listen to clients, [backlog] argument specifies max # of queued connections
    sock.listen(backlog)
    while True:
        print("Waiting to recieve message from client")
        #accept() system call is used with connection-based socket types and extracts the first connection request on the queue of pending connections.
        client, address = sock.accept()
        data = client.recv(data_payload)
        if data:
            print("Data: {}".format(data))
            client.send(data)
            print("sent {} bytes back to {}".format(data, address))
        #Close connection
        client.close()

if __name__ == "__main__"
    parser = argparse.ArgumentParser(description="Socket Server Example")
    parser.add_argument('--port', action=store, dest='port', type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)
