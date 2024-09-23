import socket
import threading

# Function to handle incoming messages from the server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')  # Receive and print messages
            print(message)
        except:
            print("An error occurred. Closing connection.")
            client_socket.close()
            break

# Function to send messages to the server
def send_messages():
    while True:
        message = input("")  # Take user input
        client_socket.send(message.encode('utf-8'))  # Send message to server

# Initialize socket and connect to server
SERVER_IP = "127.0.0.1"
SERVER_PORT = 1234
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

# Start threads for sending and receiving messages
threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()