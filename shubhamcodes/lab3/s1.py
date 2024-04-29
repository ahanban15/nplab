import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

server.settimeout(0.2)
server.bind(("", 44444))
message = b"broadcast from server"
while True:
    server.sendto(message, ('<broadcast>', 37022))
    print("message sent!")
    time.sleep(1)
