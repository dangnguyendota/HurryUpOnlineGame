import socket
import threading
from Setting import *

class Client:
    def __init__(self, parent=None):
        self.parent = parent
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.data_tmp = []

    def connect(self, host, port):
        self.socket.connect((host, port))
        recv = threading.Thread(target=self.recv_data)
        recv.start()

    def send(self, data):
        self.socket.sendall(data.encode())
        print("send" , data)

    def recv_data(self):
        while True:
            try:
                data_recv = self.socket.recv(1024).decode()
            except:
                self.socket.sendall("No data recieved!")
                break
            if data_recv == "QUIT":
                self.socket.sendall("OK tao quit")
                break
            if not data_recv:
                self.socket.close()
            if self.parent:
                self.parent.addMove(data_recv)
            self.data_tmp.append(data_recv)
            print("recieve from server:", data_recv)

# c = Client()
# c.connect(HOST, PORT)
# c.send("a")
