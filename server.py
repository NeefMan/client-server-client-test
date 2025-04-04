import socket
import sys
from collections import defaultdict

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

port = 5000

s.bind(('0.0.0.0', port))

s.listen(5)

users = defaultdict(list) # {"username": inbox["message1", "message2"]}

def collect_data(c):
    data = []
    done = False
    while not done:
        packet = c.recv(1024).decode('utf-8', 'ignore')  # Ignores invalid characters
        data.append(packet)
        if not packet:
            done = True
            print("All packets have been recieved")
    return "".join(data)

def process_message(from_user, to_user, message):
    users[to_user].append(f"From {from_user}: {message}")

def send_messages(c, user):
    messages = users[user]
    if len(messages)>=1:
        print("There are messages")
        c.sendall("$".join(messages).encode())
    else:
        print("empty inbox")
        c.sendall("No messages".encode())


def kill(c):
    c.close()
    s.close()
    sys.exit()

while True:
    c, addr = s.accept()
    print(f"Connection from: {addr}")

    data = collect_data(c).split("$")

    if len(data) >= 1:
        if data[0] == "kill":
            kill(c)
        username = data[0]
        if username not in users:
            users[username] = []

    if len(data) >= 2:
        if data[1] == "vi":
            send_messages(c, username)
        elif data[1] == "sm":
            to_user = data[2]
            if to_user not in users:
                c.sendall(f"The message could not be sent because the recipient, {to_user}, does not exist".encode())
            else:
                process_message(username, to_user, data[3])
    
    c.close()