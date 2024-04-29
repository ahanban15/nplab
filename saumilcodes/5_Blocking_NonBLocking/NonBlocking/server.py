import socket
import select
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12344))
server_socket.listen(5)
server_socket.setblocking(False)

inputs = [server_socket]

while True:
    readable, _, _ = select.select(inputs, [], [], 5)
    for sock in readable:
        if sock is server_socket:
            client_socket, client_address = server_socket.accept()
            client_socket.setblocking(False)
            inputs.append(client_socket)
            print(f"New connection from {client_address}")
        else:
            data = sock.recv(1024)
            if data:
                print(f"Received data from {sock.getpeername()}: {data.decode()} - Time:{time.strftime('%H:%M:%S')}")
            else:
                print(f"Connection closed by {sock.getpeername()} - Time:{time.strftime('%H:%M:%S')}")
        inputs.remove(sock)
        sock.close()