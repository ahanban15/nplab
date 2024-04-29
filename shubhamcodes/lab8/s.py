import socket
import signal
import sys

def signal_handler(sig, frame):
    print('Exiting...')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 9999)
print('Starting up on %s port %s' % server_address)
server_socket.bind(server_address)

while True:
    print('\nWaiting to receive message...')
    data, address = server_socket.recvfrom(4096)
    
    print('Received %s bytes from %s' % (len(data), address))
    print('Data: %s' % data.decode())
    
    if data:
        sent = server_socket.sendto(data, address)
        print('Sent %s bytes echo back to %s' % (sent, address))

