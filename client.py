# Import socket module 
import socket             
 
# Create a socket object 
s = socket.socket()         
 
# Define the port on which you want to connect 
port = 5000             
 
# connect to the server on local computer 
s.connect(('18.218.245.80', port)) 

s.sendall("user1$user2$This is a message Sigma Balls".encode())

try:
    done = False
    while not done:
        packet = s.recv(1024).decode('utf-8', 'ignore')  # Ignores invalid characters
        print(packet)
        if packet == '':
            done = True
            break
except socket.error as e:
    print(f"Socket error: {e}")