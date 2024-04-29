import socket

# Server configuration
server_ip = "127.0.0.1"
server_port = 12334

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the interface for the client socket (optional, you can omit this line)
client_socket.bind(('0.0.0.0', 0))

while True:
    # Get user input and send it to the server
    message = input("Enter a message to send to the server: ")
    client_socket.sendto(message.encode(), (server_ip, server_port))

# Close the socket (Note: This part will not be reached in this example)
client_socket.close()
