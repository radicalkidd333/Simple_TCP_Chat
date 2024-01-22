import socket
import threading
  
# Create a socket object with IPV4 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 123
# Bind the socket to a specific address and port
server_socket.bind(('127.0.0.1',port ))

# Listen for incoming connections
server_socket.listen(4) #maximum connections 
print(f"Server listening on port {port}")

# List to store connected clients
clients = []

# Function to handle client connections
def handle_client(client_socket):
    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024) #1024 means maximum amount of bytes in message 
            if not data:#if there is no message 
                break

            # Broadcast the received message to all connected clients except the sender
            for c in clients:
                if c != client_socket:
                    c.send(data) # send() sends data back to 
        except Exception as e:
            print(f"Error: {e}")
            break
    remove_client(client_socket)
def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)
       
             
        print(f"disconnected.")
# Main server loop
while True:
    # Accept a connection from a client
    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr}")
   
    # Add the new client to the list
    clients.append(client_socket)

    # Create a new thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()





    #Merge the Uf_scraper to send scraped wikkipedia data to all clients 

    #Add the nickname fuction harder that it seems 

