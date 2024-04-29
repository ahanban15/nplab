import socket

server_ip = '127.0.0.1'
server_port = 4000

ct = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    msg = input("Input message to send to server ")
    ct.sendto(msg.encode(),(server_ip,server_port))
    
    recv_msg,Serveraddr = ct.recvfrom(1024)
    print("Recieved Message : ",recv_msg.decode())