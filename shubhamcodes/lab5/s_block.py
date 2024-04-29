import socket
import time
from datetime import datetime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))

# set to blocking mode
server_socket.setblocking(True)

server_socket.listen(5)

while True:
    # Establish connection with client
    client_socket, addr = server_socket.accept()
    print('Got connection from', addr)
    # wait 5 seconds before sending message
    time.sleep(5)
    # Send data to the client
    print('message sent to client at', datetime.now().strftime("%H:%M:%S"))
    client_socket.send(b'Thank you for connecting')

    client_socket.close()

