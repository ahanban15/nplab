import socket

def defragment_message(fragments):
    fragments.sort()  # Sort fragments based on sequence numbers
    received_sequence = [int(fragment[:4]) for fragment in fragments]
    message = ''.join(fragment[4:] for fragment in fragments)  # Exclude sequence numbers
    return message, received_sequence

def main():
    host = '192.168.0.141'
    port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input("Enter message to send (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break

        client.sendto(message.encode('utf-8'), (host, port))

        received_fragments = []
        while True:
            data, addr = client.recvfrom(1024)
            fragment = data.decode('utf-8')
            received_fragments.append(fragment)

            # Check if the last fragment in the sequence has been received
            if not fragment[4:] or fragment[4] == '0':
                break

        reconstructed_message, received_sequence = defragment_message(received_fragments)
        print(f"Reconstructed message: {reconstructed_message}")
        print(f"Received sequence: {received_sequence}")

    client.close()

if __name__ == "__main__":
    main()

