import socket
import signal
import os
import select

# Define the server address and port
SERVER_ADDRESS = ('127.0.0.1', 7845)

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address and port
server_socket.bind(SERVER_ADDRESS)

print('UDP echo server is listening...')

# Signal handler function
def handle_signal(sig, frame):
    print('Shutting down the server...')
    server_socket.close()
    os._exit(0)

# Register signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, handle_signal)

# Set the server socket as non-blocking
server_socket.setblocking(False)

# List to hold sockets to be monitored
sockets = [server_socket]

while True:
    # Use select to wait for data to be ready for reading on the server socket
    readable, _, _ = select.select(sockets, [], [])

    for sock in readable:
        if sock is server_socket:
            # Accept incoming connection
            data, client_address = server_socket.recvfrom(1024)
            print(f"Received data from {client_address}: {data.decode()}")

            # Echo back the received data to the client
            server_socket.sendto(data, client_address)

