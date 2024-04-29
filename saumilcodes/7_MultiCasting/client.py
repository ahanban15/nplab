import socket
import struct

multicast_group = '224.0.0.1'
multicast_port = 2000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ttl = struct.pack('b', 1)
client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    message = input("Enter message to multicast: ")
    client_socket.sendto(message.encode('utf-8'), (multicast_group, multicast_port))