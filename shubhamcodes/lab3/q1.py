import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 37022))
while True:
    data, addr = client.recvfrom(1024)
    print("received message: %s"%data)
    time.sleep(1)
