import socket
import json
import time
import sys

s = socket.socket()

port = 5000

s.bind(('0.0.0.0', port))

s.listen(5)

users = {} # [username] = (ip, port, c_socket)

task_queue = [] # timestamp, from_user, to_user, message

while True:
    c, addr = s.accept()
    ip, port = addr
    print(f"connection from {addr}")

    delimeter = "$"

    data = c.recv(1024).decode()
    if data == "kill":
        s.close()
        sys.exit()
    
    data = data.split(delimeter) # [username, connect_to_username, message]
    if len(data):
        username = data[0]
        users[username] = (ip, port, c)
    if len(data) >= 2:
        connect_to_username = data[1]
    if len(data) >= 3:
        message = data[2]
        task_queue.append((time.time(), username, connect_to_username, message))
    
    temp = []
    task_max_buffer_time = 10
    for task in task_queue:
        timestamp, from_user, to_user, message = task
        if time.time() - timestamp < 10 and (not from_user in users or not to_user in users):
            temp.append(task) # If the task cannot be completed for the above reasons, retry next time
            continue
        unused, unused, c = users[to_user]

        c.sendall(f"{from_user}{delimeter}{message}".encode())
    task_queue = temp