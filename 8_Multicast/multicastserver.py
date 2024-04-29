import socket
import struct

def create_multicast_socket(group, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', port))
    
    # Set the TTL (time-to-live) for the multicast packet
    ttl = struct.pack('b', 1)
    server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
    
    # Add the client to the multicast group
    group_address = (group, port)
    server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(group_address[0]) + socket.inet_aton("0.0.0.0"))

    return server_socket

def run_server():
    multicast_group = '224.0.0.1'
    server_port = 5000

    server_socket = create_multicast_socket(multicast_group, server_port)

    print(f"Multicast server listening on {multicast_group}:{server_port}")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        print(f"Received message from {client_address}: {data.decode('utf-8')}")

if __name__ == "__main__":
    run_server()

