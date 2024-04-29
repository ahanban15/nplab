import socket

server_ip = '127.0.0.1'
server_port = 5000

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((server_ip,server_port))
server.listen(1)

print("Server Live\n")

c_socket,c_addr = server.accept()

while True:
    msg = c_socket.recv(1024)
    print("Message Recieved : ",msg.decode())
    print(f"Active Socket : {c_addr}")
    print(f"Passive Socket : {server_ip,server_port}")
    print(f"Client Socket : {c_socket.getsockname()}")
   
    
    

    send_msg = input("Input message to send to client")
    c_socket.send(send_msg.encode())
    print("Message Sent")