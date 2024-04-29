# client code for UDP (interfacing)
import socket

server_ip = '192.168.1.104'
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("client socket created")

message = "Hello, server!"
client_socket.sendto(message.encode('utf-8'), (server_ip, server_port))

response, server_address = client_socket.recvfrom(1024)
print(f"Received response from {server_address}: {response.decode('utf-8')}")

client_socket.close()
print("connection closed")
