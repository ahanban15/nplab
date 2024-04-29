import socket
import threading
import struct  # Import the struct module

def create_multicast_socket(group, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_socket.bind(('', 0))

    # Set the TTL (time-to-live) for the multicast packet
    ttl = struct.pack('b', 1)
    client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    return client_socket

def run_client(client_id):
    multicast_group = '224.0.0.1'
    server_port = 5000

    client_socket = create_multicast_socket(multicast_group, server_port)

    message = f"Hello from Client 2!"

    try:
        # Send data to the multicast group
        client_socket.sendto(message.encode('utf-8'), (multicast_group, server_port))
        print(f"Client 2 sent message to {multicast_group}:{server_port}: {message}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    num_clients = 1

    # Create and start multiple client threads
    threads = []
    for i in range(num_clients):
        thread = threading.Thread(target=run_client, args=(i+1,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

