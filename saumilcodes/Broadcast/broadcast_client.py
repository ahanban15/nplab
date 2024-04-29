import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

s.bind(("",37020))
while True:
    data, address = s.recvfrom(1024)
    msg = data.decode('utf-8')
    print(f"From : {address} Recieved message : {msg}")
    
    if msg == 'exit':
        break

s.close()
    