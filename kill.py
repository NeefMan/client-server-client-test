import socket
# Import socket module 
import socket             
 
# Create a socket object 
s = socket.socket()         
 
# Define the port on which you want to connect 
port = 5000             
 
# connect to the server on local computer 
s.connect(('13.58.174.226', port)) 

s.sendall("kill".encode())