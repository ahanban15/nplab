import socket

server_ip = '127.0.0.1'
server_port = 5000

ct = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ct.connect((server_ip,server_port))

while True:
    msg = input("Message to send to server")
    ct.send(msg.encode())
    recv_msg = ct.recv(1024)
    print("Recieved Message : ",recv_msg.decode())
    if(recv_msg.decode=='exit'):
        break

ct.close()

