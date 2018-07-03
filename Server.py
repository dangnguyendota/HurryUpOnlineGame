import socket
import threading
from Setting import *

class Server:
    def __init__(self, parent=None):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.parent = parent
        self.data_tmp = []

    def connect(self, host, port):
        self.thread = threading.Thread(target=self.connect_client, args=(host, port, ))
        self.thread.start()

    def connect_client(self, host, port):
        self.socket.bind((host, port))
        self.socket.listen(2)
        self.conn = []
        while len(self.conn) < 2:
            conn, addr = self.socket.accept()
            self.conn.append(conn)
            print("Connected to ", addr)
        s0 = threading.Thread(target=self.recv_data0)
        s1 = threading.Thread(target=self.recv_data1)
        s0.start()
        s1.start()

    def send(self, data):
        for conn in self.conn:
            conn.sendall(data.encode())
            print("send: ", data)

    def recv_data0(self):
        while True:
            #thang 1
            try:
                data_recv = self.conn[0].recv(1024).decode()
            except:
                self.close()
                break
            if data_recv == "QUIT":
                print("Quit request accepted!")
                self.close()
                break
            if not data_recv:
                self.close()
            print("Recv:", data_recv)
            self.conn[1].sendall(data_recv.encode())
    def recv_data1(self):
        while True:
            #thang 2
            try:
                data_recv = self.conn[1].recv(1024).decode()
            except:
                self.close()
                break
            if data_recv == "QUIT":
                print("Quit request accepted!")
                self.close()
                break
            if not data_recv:
                self.close()
            print("Recv:", data_recv)
            self.conn[0].sendall(data_recv.encode())

    def close(self):
        self.conn[0].close()
        self.conn[1].close()
        self.socket.close()

    def disconnect(self):
        self.socket.close()

# s = Server()
# s.connect(HOST, PORT)
