import socket
import random

def fragment_message(message, fragment_size):
    fragments = []
    sequence_number = random.randint(1, 1000)

    while message:
        current_fragment = f"{sequence_number:04d}" + message[:fragment_size]
        fragments.append(current_fragment)
        message = message[fragment_size:]
        sequence_number += 1

    return fragments

def defragment_message(fragments):
    fragments.sort()  # Sort fragments based on sequence numbers
    message = ''.join(fragment[4:] for fragment in fragments)  # Exclude sequence numbers
    return message

def main():
    host = '192.168.0.141'
    port = 12345
    fragment_size = 10

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))

    print(f"Server listening on {host}:{port}")

    while True:
        data, addr = server.recvfrom(1024)
        message = data.decode('utf-8')

        print(f"Received message: {message} from {addr}")

        fragments = fragment_message(message, fragment_size)

        print("Fragmented sequence:")
        for fragment in fragments:
            print(fragment)

        reconstructed_message = defragment_message(fragments)
        print(f"Reconstructed message: {reconstructed_message}")

if __name__ == "__main__":
    main()
