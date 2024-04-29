import socket

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_ip = '127.0.0.1'
port = 12333
cs.bind(('0.0.0.0', 0))
cs.connect((host_ip, port))
message = "Hello, server! This is the client."
cs.send(message.encode())
response = cs.recv(1024)
print(response)
cs.close()

