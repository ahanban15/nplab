import socket
import random
import time

server_ip = '127.0.0.1'
server_port = 4000

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind((server_ip,server_port))

attempt = 4
retry = 2

while attempt>0:
    try:
        data,ct_addr = server.recvfrom(1024)
        drop = random.randint(0,100)
        if(drop<70):
            print(f"Data from client {ct_addr} dropped")
        
        time.sleep(5)
        print(f"Recieved data from {ct_addr}")
        response = "Server : Data recieved successfully"
        server.sendto(response.encode(),ct_addr)
        attempt = 4
        retry = 2
    except Exception as e:
        print(f"Exception : retry after {retry} seconds")
        response = "dropped"
        server.sendto(response.encode(),ct_addr)
        time.sleep(retry)
        attempt-=1
        retry*=2

server.close()