import socket
import struct


multicast_group = '224.0.0.1'
multicast_port = 2000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', multicast_port))

ttl = struct.pack('b', 1)
server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
while True:
    data, address = server_socket.recvfrom(1024)
    print(f"Received message: {data.decode()} from {address}")