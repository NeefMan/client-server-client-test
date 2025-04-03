import socket
# Import socket module 
import socket             
 
# Create a socket object 
s = socket.socket()         
 
# Define the port on which you want to connect 
port = 5000             
 
# connect to the server on local computer 
s.connect(('18.218.245.80', port)) 

s.sendall("kill".encode())