# Import socket module 
import socket        
import sys     
 
# Create a socket object 
 
# Define the port on which you want to connect 
port = 5000     
delimeter = "$"        
 
# connect to the server on local computer 

username = input("What is your username?")
while True:
    s = socket.socket()        
    s.settimeout(2) 
    task = input("Would you like to send a message? (sm) Or view your inbox? (vi) Or exit? (q)")
    if task == "q":
        s.close()
        sys.exit()
    elif task == "vi":
        s.connect(('18.218.245.80', port))
        s.sendall(f"{username}{delimeter}vi".encode())
        
        data = []  # Moved here
        done = False
        while not done:
            try:
                packet = s.recv(1024).decode('utf-8', 'ignore')
                if not packet:
                    done = True
                    break
                data.append(packet)
            except socket.timeout:
                done = True  # Break cleanly on timeout

        s.close()
        
        full_data = "".join(data).strip()
        print("\n--- Inbox ---")
        if full_data == "No messages":
            print("No messages.")
        else:
            for message in full_data.split("$"):
                print(message)
        print("-------------\n")
    elif task == "sm":
        to_user = input("Who would you like to send it to?")
        message = input("What is the message?")
        s.connect(('18.218.245.80', port))
        s.sendall(f"{username}{delimeter}sm{delimeter}{to_user}{delimeter}{message}".encode())
        s.close()