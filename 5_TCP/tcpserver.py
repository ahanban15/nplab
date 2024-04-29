import socket

def start_server():
    # Server configuration
    # server_ip = "192.168.0.201"
    server_ip = "127.0.0.1"
    server_port = 12345

    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Enable address reuse
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to a specific IP address and port
    server_socket.bind((server_ip, server_port))

    # Listen for incoming connections (max 1 pending connection)
    server_socket.listen(1)

    print(f"Server listening on {server_ip}:{server_port}")

    while True:
        # Accept a connection from a client
        client_socket, client_address = server_socket.accept()

        # Print information about the connection
        print(f"Accepted connection from {client_address}")
        print(f"Local socket: {client_socket.getsockname()}")
        print(f"Peer socket: {client_socket.getpeername()}")

        # Process the connection
        received_data = receive_all(client_socket)
        print(f"Received data from {client_address}: {received_data}")

        # Send a response back to the client
        response = "Hello, client! This is the server."
        client_socket.send(response.encode())

        # Close the client socket
        client_socket.close()

def receive_all(socket):
    # Receive data from the socket until the message is complete
    data = b""
    while True:
        chunk = socket.recv(1024)
        if not chunk:
            break
        data += chunk
        if b"\0" in data:
            break
    return data.decode()

if __name__ == "__main__":
    start_server()

