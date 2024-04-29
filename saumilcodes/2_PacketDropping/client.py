import socket
import time

server_ip = '127.0.0.1'
server_port = 4000

ct = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg = "Hello Server"
ct.sendto(msg.encode(),(server_ip,server_port))

recv_msg,server_addr = ct.recvfrom(1024)

attempt=3

while(attempt>0 and recv_msg.decode()=="dropped"):
    print(f"No response, Retrying...    Attempt Left : {attempt}")
    time.sleep(2)

    ct.sendto(msg.encode(),(server_ip,server_port))
    recv_msg,server_addr = ct.recvfrom(1024)

    attempt-=1

if(attempt!=0):
    print(f"Recieved message from server : {recv_msg.decode()}")
else:
    print("Server Down")