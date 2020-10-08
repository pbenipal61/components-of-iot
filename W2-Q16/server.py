import socket

HOST = 'localhost'
PORT = 22222

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
    s.bind((HOST, PORT))
    s.listen()
    connection, address = s.accept()
    with connection:
        print(f"Connected: {address}")
        while True:
            data = connection.recv(1024)
            updated_data = f"Server response: {data.decode('ascii')}"
            if not data:
                break
            connection.send(updated_data.encode('ascii'))