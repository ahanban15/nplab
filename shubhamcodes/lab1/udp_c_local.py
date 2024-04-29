# client code for UDP (localhost)
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("client socket created")

server_port = 1222
server_ip = socket.gethostbyname(socket.gethostname())

message = "Hello, server!"
client.sendto(message.encode('utf-8'), (server_ip, server_port))

response, server_address = client.recvfrom(1024)
print(f"Received response from {server_address}: {response.decode('utf-8')}")

client.close()
print("connection closed")
