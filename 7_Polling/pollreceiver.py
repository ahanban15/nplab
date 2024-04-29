import socket
import select

# Client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Create a poll object
poll = select.poll()

# Register the client socket for polling
poll.register(client_socket, select.POLLOUT | select.POLLIN | select.POLLPRI | select.POLLERR | select.POLLHUP)

# Function to receive message from server
def receive_message():
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
        if event & select.POLLIN:
            # Data available to read
            message = receive_message()
            if message is False:
                print('Server closed the connection')
                exit()
            print(f'Received message from server: {message["data"].decode("utf-8")}')

        elif event & select.POLLOUT:
            # Socket ready for writing
            message = input("Enter your message: ")
            send_message = f'{len(message):<4}'.encode('utf-8') + message.encode('utf-8')
            client_socket.send(send_message)

# Close the client socket
client_socket.close()
