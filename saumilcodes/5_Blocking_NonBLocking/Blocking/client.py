import socket
from datetime import datetime


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
send_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
message = "Hello, server at {}".format(send_time)
client_socket.send(message.encode())
data = client_socket.recv(1024)
receive_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Received data:", data.decode(), "at", receive_time)


client_socket.close()