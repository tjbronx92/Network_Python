## Sockets

**_socket_ - a socket is one endpoint of a two-way communication link between two programs running on the network.**

Create socket:

```python
socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```
Creating a socket requires:
1. define address family (default=AF_INET (IPv4))
2. define socket type (default=SOCK_STREAM (TCP))

