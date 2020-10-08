import socket

HOST = 'localhost'
PORT = 22222

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
    s.connect((HOST, PORT))
    s.sendall(b"The task has finished")
    data = s.recv(1024)
    
print(repr(data))