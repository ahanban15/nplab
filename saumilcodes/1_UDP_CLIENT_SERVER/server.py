import socket

server_ip = '127.0.0.1'
server_port = 4000

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind((server_ip,server_port))

print("Server Live")

while True:
    data,c_addr = server.recvfrom(1024)
    print("Message Received : ",data.decode())

    msg = input("Input data to send to client : ")
    server.sendto(msg.encode(),c_addr)