import socket
import struct
import random

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = "I am a B.Tech 3rd year student at NIT Delhi"
    fragment_size = 2

    seq_no = random.randint(1, 255)  # Randomly initialize first sequence number

    for i in range(0, len(message), fragment_size):
        fragment = message[i:i+fragment_size]
        packet = struct.pack('!HB', seq_no, fragment_size) + fragment.encode()
        # client_socket.sendto(packet, ('192.168.0.201', 5555))
        client_socket.sendto(packet, ('127.0.0.1', 5555))
        print(f"Sent fragment {seq_no} with data: {fragment}")
        seq_no += 1

if __name__ == "__main__":
    client()

