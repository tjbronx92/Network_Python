#!/usr/bin/env python3

''' Requirement - ntplib.py must be downloaded
https://pypi.org/project/ntplib/'''

import ntplib
from time import ctime

def print_time():
    #Create NTP Client
    ntp_client = ntplib.NTPClient()
    #NTP server request
    response = ntp_client.request('ntp.multacom.com')
    print(ctime(response.tx_time))

if __name__ == '__main__':
    print_time()
