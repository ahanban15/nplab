import socket
import random
import time

server_ip = '127.0.0.1'
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))

retry_attempts = 5
retry_delay = 2  # Initial retry delay in seconds

while retry_attempts > 0:
    try:
        data, client_address = server_socket.recvfrom(1024)

        # Simulate dropping 70% of data
        drop_probability = random.random()
        if drop_probability < 0.7:
            print(f"Data from {client_address} dropped.")
            raise Exception("Data dropped")  # Trigger the except block

        print(f"Received data from {client_address}: {data.decode('utf-8')}")

        response = "Server: Data received successfully"
        server_socket.sendto(response.encode('utf-8'), client_address)
        break  # Exit the retry loop if data is successfully processed

    except Exception as e:
        print(f"Exception: {e}. Retrying after {retry_delay} seconds...")
        time.sleep(retry_delay)
        retry_attempts -= 1
        retry_delay *= 2  # Increase the retry delay exponentially

# Cleanup: Close the server socket after handling requests
server_socket.close()

