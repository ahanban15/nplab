import socket

def start_client():
    # Server configuration
    # server_ip = "192.168.0.201"
    server_ip = "127.0.0.1"
    server_port = 12345

    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set the interface for the client socket (optional, you can omit this line)
    client_socket.bind(('0.0.0.0', 0))

    # Connect to the server
    client_socket.connect((server_ip, server_port))
    print(f"Connected to server at {server_ip}:{server_port}")

    # Send data to the server
    message = "Hello, server! This is the client."
    send_all(client_socket, message)

    # Receive and process response from the server
    response = receive_all(client_socket)
    print(f"Received response from server: {response}")

    # Close the socket
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


def send_all(socket, message):
    # Send the entire message in chunks until the end
    socket.sendall(message.encode() + b"\0")

if __name__ == "__main__":
    start_client()