import socket
import time
from datetime import datetime
import threading

def get_time():
    return datetime.now().strftime("%H:%M:%S")

def handle_client_connection(client_socket):
    try:
        # Receive data from the client
        data = client_socket.recv(1024)
        # Print the message sent by the client
        print('Message from client:', data.decode(), 'at', get_time())
    except OSError as e:
        print("Error receiving data from client:", e)
    finally:
        client_socket.close()

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set non-blocking mode
server_socket.setblocking(0)

host = socket.gethostname()
port = 9999

server_socket.bind((host, port))

server_socket.listen(5)

while True:
    try:
        # Establish connection with client
        client_socket, addr = server_socket.accept()
        print('Got connection from', addr, 'at', get_time())

        # Create a thread to handle the client connection
        client_handler = threading.Thread(target=handle_client_connection, args=(client_socket,))
        client_handler.start()

    except BlockingIOError:
        pass

    print('Server is listening at', get_time())
    time.sleep(1)  

