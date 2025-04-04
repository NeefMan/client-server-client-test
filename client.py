import socket
import sys

# Create a socket object
s = socket.socket()
s.settimeout(5)  # Set a timeout of 5 seconds

# Server details
host = '18.218.245.80'
port = 5000
delimiter = "$"

username = input("What is your username? ")

while True:
    # Ask for user input
    task = input("Would you like to send a message? (sm) Or view your inbox? (vi) Or exit? (q): ")

    if task == "q":  # Exit
        s.close()
        sys.exit()

    elif task == "vi":  # View inbox
        s.connect((host, port))
        s.sendall(f"{username}{delimiter}vi".encode())
        
        try:
            response = s.recv(1024).decode('utf-8', 'ignore')
            if response:
                print(f"Inbox: {response}")
            else:
                print("No response from the server.")
        except socket.timeout:
            print("Request timed out.")

        s.close()

    elif task == "sm":  # Send message
        to_user = input("Who would you like to send it to? ")
        message = input("What is the message? ")
        
        s.connect((host, port))
        s.sendall(f"{username}{delimiter}sm{delimiter}{to_user}{delimiter}{message}".encode())
        
        s.close()
