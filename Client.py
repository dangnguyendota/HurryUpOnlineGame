import socket
import threading

def createClient():
    client = socket.socket()
    host = "localhost"
    port = 5000
    client.connect((host, port))
    s = threading.Thread(target=sendData, args=client)
    s.start()
    s.join()

def sendData(client):
    while True:
        msg = "CC"
        client.send(msg.encode())

createClient()