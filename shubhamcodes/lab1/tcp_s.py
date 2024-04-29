# server code for TCP
import socket
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server socket created")

port = 1222
host_ip = socket.gethostbyname(socket.gethostname())

server.bind((host_ip, port))
print("socket bound to port", port)

server.listen(5)
print("server is listening")

while True:
	client, address = server.accept()
	print("Got connection from ", address)
	
	client.send("Thank you for connecting".encode('utf-8'))
	print("client message:\n",client.recv(1024).decode('utf-8'))
	
	client.close()
	print(f"connection with {address} closed")
