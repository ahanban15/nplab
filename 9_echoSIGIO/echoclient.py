import socket
import signal
import os
import select

# Define the server address and port
SERVER_ADDRESS = ('127.0.0.1', 7845)

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Signal handler function
def handle_signal(sig, frame):
    print('Closing the client...')
    client_socket.close()
    os._exit(0)

# Register signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, handle_signal)

# Set the client socket as non-blocking
client_socket.setblocking(False)

# List to hold sockets to be monitored
sockets = [client_socket]

while True:
    # Get user input if the socket is ready for writing
    _, writable, _ = select.select([], sockets, [])

    for sock in writable:
        if sock is client_socket:
            # Get user input
            message = input("Enter message to send (type 'exit' to quit): ")

            if message.lower() == 'exit':
                client_socket.close()
                os._exit(0)

            # Send the message to the server
            client_socket.sendto(message.encode(), SERVER_ADDRESS)

    # Check if there's data ready for reading from the server
    readable, _, _ = select.select(sockets, [], [])

    for sock in readable:
        if sock is client_socket:
            # Receive the echoed message from the server
            echoed_message, server_address = client_socket.recvfrom(1024)
            print(f"Received echo from server {server_address}: {echoed_message.decode()}")

