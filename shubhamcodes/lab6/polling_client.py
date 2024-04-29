import socket

# Client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.0.218', 12345))

# Function to send message to server
def send_message(message):
    message_header = f'{len(message):<4}'.encode('utf-8')
    client_socket.send(message_header + message)

while True:
    # Send message to server
    message = input("Enter your message: ")
    if message.lower() == 'exit':
        break
    send_message(message.encode('utf-8'))

client_socket.close()
