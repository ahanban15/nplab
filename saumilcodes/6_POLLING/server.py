import socket
import select

HOST = '127.0.0.1'
PORT = 65432

client_sockets = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))
server_socket.listen(1)
print("Server is listening for connections...")


def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            client_sockets.remove(client_socket) 
            client_socket.close()
            break
        else:
            print("Received:", data.decode())
    
while True:
    ready_to_read,_,_ = select.select([server_socket] + client_sockets, [], [], 0)
    for sock in ready_to_read:
        if sock is server_socket:
            client_socket, client_address = server_socket.accept() 
            print("Connected to:", client_address) 
            client_sockets.append(client_socket)
        else:
            handle_client(sock)
