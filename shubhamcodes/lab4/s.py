import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_ip = '127.0.0.1'
port = 12333

#s.setsockopt(s, SOL_SOCKET, SO_REUSEADDR, 1)

s.bind((host_ip, port))
s.listen(1)
print('listening at', s.getsockname())

while True:	
	client, addr = s.accept()
	message = 'Welcome to the server!'
	client.sendall(message.encode('utf-8'))
	print('client: ', client.getsockname())
	print('client peer: ', client.getpeername())
	data = client.recv(1024)
	print(f"Received data from {addr}: {data.decode()}")
	client.close()
	break
s.close()	
	
