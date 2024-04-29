import socket
import signal
import os

def signal_handler(signum, frame):
    print(f"Received signal (signum), exiting...")
    os._exit(6)

def udp_echo_server (host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP echo server is listening on {host}:{port}")
    while True:
        data, client_address = server_socket.recvfrom(1024)
        print(f"Received data from {client_address}: {data.decode()}")
        server_socket.sendto(data, client_address)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    host = 'localhost'  
    port = 9999
    udp_echo_server(host, port)