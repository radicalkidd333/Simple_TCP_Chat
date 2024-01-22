import socket
import threading
import sys 
import time
import test_bob  
from playsound import playsound

#from playsound import playsound 
# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
nickname = input("Enter a nickname: ")
nick = nickname + ": "
# Connect to the server
client_socket.connect(('localhost', 123))
path = "/home/radicalkidd/Downloads/Discord notification - sound effect [rIPq9Fl5r44].mp3"
# Function to receive messages from the server
def receive_messages():
    while True:
        try:
            
            # Receive data from the server
            playsound(path)
            data = client_socket.recv(1024)
            print(data.decode('utf-8'))    
            playsound(path)
 
        except Exception as e:
            print(f"Error: {e}")
            break

def exit_program():
    exit_message =f"{nick} has left..".encode('utf-8')
    client_socket.send(b'exit')
    time.sleep(1)
    client_socket.send(exit_message)
    client_socket.close()
    sys.exit()
def who_is():
    test_bob()  
    
    
# Create a thread to handle receiving messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()







# Main client loop to send messages
while True:
    # Get user input
    message = input()
    if message.lower() == '!exit':
        print(f"{nickname} has left ...")
        exit_program()
    
    if message.lower() == '!who':
        who_is()

    # Send the message to the server
    client_socket.send(bytes(nick,'utf-8'))
    client_socket.send(bytes(message, 'utf-8'))
    playsound(path)
#make an exi = nicknameyword to close the program !exit
#find out how play just once 
