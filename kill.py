import socket
# Import socket module 
import socket             
 
# Create a socket object 
s = socket.socket()         
 
# Define the port on which you want to connect 
port = 5000             
 
# connect to the server on local computer 
s.connect(('3.136.151.92', port)) 

s.sendall("kill".encode())