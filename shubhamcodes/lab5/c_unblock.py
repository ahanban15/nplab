import socket
import time
import select
from datetime import datetime

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

# Set non-blocking mode
client_socket.setblocking(0)

# Connect to the server
try:
    client_socket.connect((host, port))
except BlockingIOError:
    pass

print('Client connects to server at', datetime.now().strftime("%H:%M:%S"))
# Delay before sending message
time.sleep(5)

# Send data to the server
client_socket.send(b'Hello from client')
print('Message sent to server at', datetime.now().strftime("%H:%M:%S"))

client_socket.close()

