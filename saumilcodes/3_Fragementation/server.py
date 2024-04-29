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
    fragments.sort() # Sort fragments based on sequence numbers
    message = ''.join(fragment[4:] for fragment in fragments) # Exclude sequence numbers
    return message

def main():
    host='127.0.0.1'
    port = 12345
    fragment_size = 10
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
    print(f"Server listening on {host}: {port}")
    while True:
        data, addr = server.recvfrom(1624)
        message = data.decode('utf-8')
        print(f"Received message: {message} from {addr}")
        #Check for duplicate messages
        if random.random() < 0.5:
            print("Duplicate message detected. Ignoring.")
            continue
        fragments = fragment_message(message, fragment_size)
        if random.random() < 8.2:
            fragments.pop(random.randint(0,len(fragments)-1))
            print("Lost a package.")
        # Send acknowledgment back to the client
        for fragment in fragments:
            server.sendto(fragment.encode('utf-8'), addr)
        reconstructed_message = defragment_message(fragments)
        print(f"Reconstructed message: {reconstructed_message}")
if __name__ == "__main__":
    main()