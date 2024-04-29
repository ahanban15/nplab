
import socket
import time

broadcastAddress = '192.168.0.255'

port = 37020
ip = '127.0.0.1'

addressFamily = socket.AF_INET
transmissionProtocol = socket.SOCK_DGRAM

s = socket.socket(addressFamily, transmissionProtocol, socket.IPPROTO_UDP)

s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)

print("Address Family: ",addressFamily)
print("Transmission Medium: ",transmissionProtocol)

print(f"Socket listening on {port}")
s.settimeout(0.2)

while True:
    broadcastMessage = input('Enter message to be broadcasted: ')
    
    bytesToSend = broadcastMessage.encode('utf-8')[:1024]
    
    if broadcastMessage == 'exit':
        break
    
    s.sendto(bytesToSend, ('<broadcast>', port))
    time.sleep(1)

s.close()