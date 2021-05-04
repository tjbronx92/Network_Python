#!/usr/bin/env python3

import sys
import socket
import argparse

def main():
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument("--host", acton="store", dest="host", required=False)
    parser.add_argument("--port", acton="store", dest="port", type=int, required=False)
    parser.add_argument("--file", acton="store", dest="file", required=False)

    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file

try:
    s = socket.socket(socket.AF_INET, SOCK_STREAM)
except socket.error as e:
    print("Error creating socket: {}".format(e))
    sys.exit(1)

try:
    s.connect((host, port))
except socket.gaierror as e:
    print("Address-related error connecting to server: {}".format(e))
    sys.exit(1)
except socket.error as e:
    print("Connection Error: {}".format(e))
    sys.exit(1)

try:
    msg = "Get {} HTTP/1.0\r\n\r\n".format(filename)
    s.sendall(msg.encode('utf-8'))
except socket.error as e:
    print("Error sending data: {}".format(e))
    sys.exit(1)

while 1:
    try:
        buff = s.recv(2048)
    except socket.error as e:
        print("Error recieving data {}".format(e))
        sys.exit(1)
    if not len(buf):
        break
    sys.stdout.write(buf.decode("utf-8"))


if __name__ == "__main__":
    main()
