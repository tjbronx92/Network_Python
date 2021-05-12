# Sockets

**_socket_ - a socket is one endpoint of a two-way communication link between two programs running on the network.**

## Create socket: ##
```python
socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```
Creating a socket requires:
1. define address family (default=AF_INET (IPv4))
2. define socket type (default=SOCK_STREAM (TCP))

***

## Set Socket Options: ##
```python
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
```

Setting socket options requires:
1. socket option level
2. socket option
3. True (1) or False (0) --optional 
