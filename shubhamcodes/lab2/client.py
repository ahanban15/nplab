import socket

server_ip = '192.168.0.196'
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "Hello, server!"
client_socket.sendto(message.encode('utf-8'), (server_ip, server_port))
try:
	response, server_address = client_socket.recvfrom(1024)
	print(f"Received response from {server_address}: {response.decode('utf-8')}")
	client_socket.close()
except:
	print("packet dropped")
