import socket
import threading

def createServer():
    server = socket.socket()
    host = "localhost"
    port = 5000
    server.bind((host, port))
    server.listen(1)
    conn, addr = server.accept()
    r = threading.Thread(target=receive, args=conn)
    r.start()
    r.join()

def receive(conn):
    while True:
        print("wait for data!")
        data = conn.recv(1024).decode()
        print("data recv")
        if not data:
            break
        print(data)

createServer()
