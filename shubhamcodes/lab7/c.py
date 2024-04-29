import socket
import struct

# Define the multicast group and port
MULTICAST_GROUP = '224.3.29.71'
MULTICAST_PORT = 10000

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the time-to-live for messages to reach only within the local network
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, struct.pack('b', 1))

# Send data to the multicast group
while True:
    message = input("Enter message to multicast: ")
    sock.sendto(message.encode(), (MULTICAST_GROUP, MULTICAST_PORT))
    
    
