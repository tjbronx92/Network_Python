# Sockets

**_socket_ - one endpoint of a two-way communication link between two programs running on the network.**
[socket()](https://docs.python.org/3/library/socket.html#module-socket)

## Create Socket: ##
```python
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```
Creating a socket requires:
1. define address family (default=AF_INET (IPv4))
2. define socket type (default=SOCK_STREAM (TCP))

***
# Socket Options

**getsockopt()** and **setsockopt()** manipulate options for the socket.[getsockopt(2)](https://man7.org/linux/man-pages/man2/getsockopt.2.html#DESCRIPTION)  
Options may exist at multiple protocol levels; they are always present at the uppermost socket level. [socket(7)](https://manpages.debian.org/buster/manpages/socket.7.en.html)

## Set Socket Options: ##
```python
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
```

## Get Socket Options: ##
```python
sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
```

Socket options requires:
1. socket option level
2. socket option
3. True (1) or False (0) --_setsockopt()_ optional value 
***

# Binding Sockets
When a socket is created with **socket()**, it exists in a name space (address family) but has no address assigned to it. **bind()** assigns an address to the socket. [bind(2)](https://man7.org/linux/man-pages/man2/bind.2.html)

## Bind Socket: ##
```python
sock.bind(("127.0.0.1", 0))
```

Bind requires:
1. IP address (str) --The format of address depends on the address family.
2. port number (int)
3. The socket must not already be bound --close()
***

<p align="center">
  <img src="https://files.realpython.com/media/sockets-tcp-flow.1da426797e37.jpg" alt="client_server_model" width="650">
</p>
