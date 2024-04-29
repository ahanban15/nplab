import socket
import struct 

# Define the multicast group and port
MULTICAST_GROUP = '224.3.29.71'
MULTICAST_PORT = 10000

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
sock.bind(('', MULTICAST_PORT))

# Tell the operating system to add the socket to the multicast group
group = socket.inet_aton(MULTICAST_GROUP)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Receive/respond loop
while True:
    data, address = sock.recvfrom(1024)
    print(f"Received multicast message: {data.decode()} from {address}")


