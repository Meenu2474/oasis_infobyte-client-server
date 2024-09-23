import socket
import threading

# Function to handle individual client connections
def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')  # Receive message from client
            if not message:
                break
            print(f"{client_address}: {message}")
            broadcast(message, client_socket)
        except:
            client_socket.close()
            break

# Function to broadcast messages to all connected clients
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))  # Send message to other clients
            except:
                client.close()
                clients.remove(client)

# Main function to start the server
def start_server():
    server_socket.listen()  # Start listening for incoming connections
    print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")
    while True:
        client_socket, client_address = server_socket.accept()  # Accept new client connection
        clients.append(client_socket)  # Add client to the list
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()  # Start new thread

# Initialize socket
SERVER_IP = "127.0.0.1"
SERVER_PORT = 1234
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

clients = []

if __name__ == "__main__":
    print("Starting the server...")
    start_server()
