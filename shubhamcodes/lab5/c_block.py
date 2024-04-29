import socket
from datetime import datetime

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

# Connect to the server
client_socket.connect((host, port))
# get current time
print("current time:",datetime.now().strftime("%H:%M:%S"))

# Receive data from the server
data = client_socket.recv(1024)
print('Received from server:', data.decode())
print("current time:",datetime.now().strftime("%H:%M:%S"))

client_socket.close()

