import socket

HOST = '127.0.0.1'
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("Connected to server.")

def send_message(message):
    client_socket.sendall(message.encode())

while True:
    message = input("Enter message to send (or 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    
    send_message(message)
client_socket.close()