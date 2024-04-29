# server code for UDP (localhost)
import socket
  
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Server socket created")

port = 1222
host_ip = socket.gethostbyname(socket.gethostname())

server.bind((host_ip, port))
print("socket bound to port", port)

while True:
    data, client_address = server.recvfrom(1024)
    print(f"Received data from {client_address}: {data.decode('utf-8')}")

    response = "Data received successfully"
    server.sendto(response.encode('utf-8'), client_address)
