import socket
import time
from datetime import datetime

port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', port))
server_socket.listen(1)

print(f"Server listening on port {port}")

connection, address = server_socket.accept()
print("Connected by", address)
send_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
time.sleep(5)

message = "Hello, server at {}".format(send_time)
connection.send(message.encode())
receive_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
data = connection.recv(1024)
print("Received data:", data.decode(), "at", receive_time)
connection.close()
server_socket.close()