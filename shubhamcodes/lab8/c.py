import socket

server_address = ('localhost', 9999)

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Send data
    message = input("Enter message to send: ")
    client_socket.sendto(message.encode(), server_address)

    # Receive response
    print("Waiting for response...")
    response, _ = client_socket.recvfrom(4096)
    print("Received echo response: ", response.decode())

finally:
    print("Closing socket")
    client_socket.close()

