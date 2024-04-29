import socket
from datetime import datetime

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Get the current time before sending
    send_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = "Hello, server at {}".format(send_time)
    client_socket.send(message.encode())

    data = client_socket.recv(1024)

    # Get the current time after receiving
    receive_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Received data:", data.decode(), "at", receive_time)

except Exception as e:
    print("Error:", e)

finally:
    # Shutdown and close the connection
    if 'client_socket' in locals():
        client_socket.shutdown(socket.SHUT_RDWR)
        client_socket.close()
