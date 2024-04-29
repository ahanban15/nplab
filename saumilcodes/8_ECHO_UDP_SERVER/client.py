import socket

def udp_echo_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = input("Enter message to send: ")
    client_socket.sendto(message.encode('utf-8'), (host, port))

    data,_ = client_socket.recvfrom(1024)
    print(f"Received echo from server: {data.decode('utf-8')}")
    client_socket.close()

if __name__ == "__main__":
    host = 'localhost'
    port = 9999
    udp_echo_client (host, port)