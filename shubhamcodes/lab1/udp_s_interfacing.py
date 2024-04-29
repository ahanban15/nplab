# server code for UDP (interfacing)
import socket

server_ip = '192.168.1.104'
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Server socket created")
server_socket.bind((server_ip, server_port))

while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received data from {client_address}: {data.decode('utf-8')}")

    response = "Server: Data received successfully"
    server_socket.sendto(response.encode('utf-8'), client_address)
    