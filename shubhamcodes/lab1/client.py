import socket

client = socket.socket()
print("client socket created")

server_port = 1222
server_ip = socket.gethostbyname(socket.gethostname())
print(f"sending connection request to {server_ip} server...")

client.connect((server_ip, server_port))
print("Connected successfully")

client.send("Hello".encode('utf-8'))
print("server message:\n", client.recv(1024).decode('utf-8'))

client.close()
print("connection closed")

