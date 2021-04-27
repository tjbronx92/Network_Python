import socket

def find_service_name():
    protocolname = 'tcp'
    for port in [80, 25, 21, 3389]:
        print("PORT: {} => Service Name: {}".format(port, socket.getservbyport(port, protocolname)))

    print("Port: {} => Service Name: {}".format(53, socket.getservbyport(53, "udp")))

if __name__ == '__main__':
    find_service_name()
