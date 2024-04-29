import socket
import time
from datetime import datetime

port = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind(('localhost', port))
    server_socket.listen(1)
    print(f"Server listening on port {port}")

    connection, address = server_socket.accept()
    print("Connected by", address)

    # Get the current time before sending
    send_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time.sleep(5)
    message = "Hello, server at {}".format(send_time)
    connection.send(message.encode())

    # Get the current time after receiving
    receive_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = connection.recv(1024)
    print("Received data:", data.decode(), "at", receive_time)

except Exception as e:
    print("Error:", e)

finally:
    # Shutdown and close the connection
    if 'connection' in locals():
        connection.shutdown(socket.SHUT_RDWR)
        connection.close()
    server_socket.close()
