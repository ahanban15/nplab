import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enable broadcasting mode
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Bind the socket to a specific address and port
client.bind(('', 37022))

while True:
    try:
        # Receive data from the server
        data, addr = client.recvfrom(1024)
        print(f"Received broadcast from {addr}: {data.decode('utf-8')}")
    except socket.timeout:
        # Handle timeout (no data received within the specified time)
        pass
