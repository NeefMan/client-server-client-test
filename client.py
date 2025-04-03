# Import socket module 
import socket        
import sys     
 
# Create a socket object 
s = socket.socket()         
 
# Define the port on which you want to connect 
port = 5000             
 
# connect to the server on local computer 
s.connect(('18.218.245.80', port))

username = input("What is your username?")
while True:
    task = input("Would you like to send a message? (sm) Or view your inbox? (vi) Or exit? (q)")
    if task == "q":
        sys.exit()
    elif task == "vi":
        done = False
        while not done:
            packet = s.recv(1024).decode('utf-8', 'ignore')  # Ignores invalid characters
            print(packet)
            if packet == '':
                done = True
                break
    elif task == "sm":
        to_user = input("Who would you like to send it to?")
        message = input("What is the message?")
        delimeter = "$"
        s.sendall(f"{username}{delimeter}{to_user}{delimeter}{message}")