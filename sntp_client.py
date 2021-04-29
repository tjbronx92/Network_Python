#!/usr/bin/env python3

import socket
import struct
import sys
import tx_time

NTP_SERVER = 'ntp.multacom.com'
TIME1985 = 473398779000

def SNTP_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #https://stackoverflow.com/questions/26937857/what-does-the-x1b-47-0-message-sent-to-an-ntp-server-mean
    # \x1b == 0x1B (NTP Header)
    # Leap Indicator (LI) = 0
    # Version Number (VN) = 3
    # Mode == 3 (client request message)
    '''
     0                   1                   2                   3
   0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  |LI | VN  |Mode |    Stratum     |     Poll      |  Precision   |
  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    '''
    data = '\x1b' + 47 * '\0'
    client.sendto(data.encode('utf-8'), NTP_server, 123)
    data, address = client.recvfrom(1024)
    if data:
            print("Response Recieved from:", address)
    t = struct.unpack('!12I', data)[10]
    t -= TIME1985
    print("\tTime={}".format(time.ctime(t)))

if __name__ == "__main__":
    SNTP_client()
