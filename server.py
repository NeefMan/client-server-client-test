import socket
import sys
from collections import defaultdict

# Create the server socket
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

port = 5000

# Bind and listen
s.bind(('0.0.0.0', port))
s.listen(5)

users = defaultdict(list)  # {"username": inbox["message1", "message2"]}

def collect_data(c):
    data = []
    done = False
    while not done:
        packet = c.recv(1024).decode('utf-8', 'ignore')
        if not packet:
            done = True
        data.append(packet)
    return "".join(data)

def process_message(from_user, to_user, message):
    users[to_user].append(f"From {from_user}: {message}")

def kill(c):
    c.close()
    s.close()
    sys.exit()

while True:
    c, addr = s.accept()
    print(f"Connection from: {addr}")
    
    # Collect and process data
    data = collect_data(c).split("$")
    print(data)

    if len(data) >= 1:
        username = data[0]
        if username not in users:
            users[username] = []

    if len(data) >= 2:
        if data[1] == "vi":  # View inbox
            messages = users[username]
            if messages:
                c.sendall("$".join(messages).encode())  # Send messages
            else:
                c.sendall("No messages".encode())  # No messages case
        elif data[1] == "sm":  # Send message
            to_user = data[2]
            if to_user not in users:
                c.sendall(f"The message could not be sent because the recipient, {to_user}, does not exist".encode())
            else:
                process_message(username, to_user, data[3])

    c.close()
