import socket
import struct

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # server_socket.bind(('192.168.0.201', 5555))
    server_socket.bind(('127.0.0.1', 5555))

    print("Server is listening...")

    expected_seq_no = None

    while True:
        data, addr = server_socket.recvfrom(1024)
        seq_no, fragment_size = struct.unpack('!HB', data[:3])
        fragment = data[3:].decode()

        if expected_seq_no is None:
            expected_seq_no = seq_no

        if seq_no == expected_seq_no:
            print(f"Received fragment {seq_no} with data: {fragment}")
            expected_seq_no += 1
        else:
            print(f"Out-of-sequence fragment received. Expected {expected_seq_no}, got {seq_no}")

        # You can implement message reassembly logic here

if __name__ == "__main__":
    server()

