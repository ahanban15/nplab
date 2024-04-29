import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_ip = '192.168.0.143'
port = 12333

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host_ip, port))
s.listen(2)
print('listening at', s.getsockname())

while True:	
	active, client = s.accept()
	message = 'Welcome to the server!'
	active.sendall(message.encode('utf-8'))
	print('passive socket: ', s.getsockname())
	print('active socket: ', active.getsockname())
	print('socket peer: ', active.getpeername())
	print('client: ', client)
	data = active.recv(1024)
	print(f"Received data from {client}: {data.decode()}\n")


s.close()	
	
