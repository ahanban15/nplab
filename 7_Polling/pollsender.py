import socket
import select

# Server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

# Create a poll object
poll = select.poll()

# Register the server socket for polling
poll.register(server_socket, select.POLLIN | select.POLLPRI | select.POLLERR | select.POLLHUP)

# Dictionary to map sockets to their respective data
clients = {}

# Function to receive messages from client
def receive_message(client_socket):
    try:
        message_header = client_socket.recv(4)
        if not len(message_header):
            return False
        message_length = int(message_header.decode('utf-8').strip())
        return {'header': message_header, 'data': client_socket.recv(message_length)}
    except:
        return False

while True:
    # Poll for events
    events = poll.poll()

    for fd, event in events:
        # If server socket is readable, accept new connection
        if fd == server_socket.fileno():
            client_socket, client_address = server_socket.accept()
            poll.register(client_socket, select.POLLIN | select.POLLPRI | select.POLLERR | select.POLLHUP)
            clients[client_socket.fileno()] = {'socket': client_socket, 'user': ''}
            print('Accepted new connection from {}:{}'.format(*client_address))
        else:
            # Received an event from an existing client socket
            client_socket = clients[fd]['socket']
            user = clients[fd]['user']

            if event & select.POLLIN:
                # Data available to read
                message = receive_message(client_socket)
                if message is False:
                    print('Closed connection from: {}'.format(user))
                    poll.unregister(client_socket)
                    client_socket.close()
                    del clients[fd]
                    continue
                print(f'Received message from {user}: {message["data"].decode("utf-8")}')

                # Sending a reply back to the client
                reply_message = f"Server received: {message['data'].decode('utf-8')}. Thank you!"
                send_message = f'{len(reply_message):<4}'.encode('utf-8') + reply_message.encode('utf-8')
                client_socket.send(send_message)

            elif event & select.POLLOUT:
                # Socket ready for writing (not used in the server)
                pass

# Close the server socket
server_socket.close()


