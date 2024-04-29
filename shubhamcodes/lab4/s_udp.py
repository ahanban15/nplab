import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host_ip = '127.0.0.1'
port = 12334
s.bind((host_ip, port))

print(f"Server listening on {host_ip}:{port}")

while True:	
	data, c_addr = s.recvfrom(1024)
	
	print(f"Received data from {c_addr}: {data.decode()}")

s.close()	
	
