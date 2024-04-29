import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enable broadcasting mode
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Set a timeout 
server.settimeout(0.2)

while True:
    # Get user input for the message
    user_input = input("Enter your message: ")
    message = user_input.encode('utf-8')  

    server.sendto(message, ('<broadcast>', 37022))
    print("Broadcasted message: ", user_input)
    time.sleep(1)
