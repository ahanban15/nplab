# 2 second delay on client side
'''
import socket
import time

server_ip = '192.168.0.196'
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "Hello, server!"
client_socket.sendto(message.encode('utf-8'), (server_ip, server_port))

response, server_address = client_socket.recvfrom(1024)
print(f"Received response from {server_address}: {response.decode('utf-8')}")

# If the response is not received, retry every 2 seconds
retry_attempts = 5
while retry_attempts > 0 and not response:
    print("No response received. Retrying...")
    time.sleep(2)

    # Send the message again
    client_socket.sendto(message.encode('utf-8'), (server_ip, server_port))
    response, server_address = client_socket.recvfrom(1024)

    retry_attempts -= 1

# Close the socket after handling requests
# client_socket.close()
'''




