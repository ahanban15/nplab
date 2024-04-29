import socket
import random
import time

def fragment_message(message, fragment_size):
    fragments = []
    sequence_number = random.randint(1, 1000)
    while message:
        current_fragment = f"{sequence_number: 84d}" + message[:fragment_size]
        fragments.append(current_fragment)
        message = message[fragment_size:]
        sequence_number += 1
    return fragments
def defragment_message(fragments):
    fragments.sort() # Sort fragments based on sequence numbers
    received_sequence = [int (fragment[:4]) for fragment in fragments]
    message=''.join(fragment [4:] for fragment in fragments) # Exclude sequence numbers
    return message, received_sequence

def main():
    host = '127.0.0.1'
    port = 12345
    fragment_size = 10
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        message = input("Enter message to send (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        fragments = fragment_message(message, fragment_size)
        for fragment in fragments:
            client.sendto(fragment.encode('utf-8'), (host, port)) 
            time.sleep(6.1) # Introduce a delay to simulate network latency
        received_fragments = []
        while True:
            data, addr = client.recvfrom(1824) 
            fragment = data.decode('utf-8')
            received_fragments.append(fragment)
            #Check if the last fragment in the sequence has been received
            if not fragment [4:] or fragment [4] == '0':
                break
        reconstructed_message, received_sequence = defragment_message(received_fragments)
        print(f"Reconstructed message : (reconstructed_message)")
        print(f"Received sequence: {received_sequence}")
    client.close()

if __name__ == "__main__":
    main()
1