# Insecure code with uncontrolled resource consumption (socket connections)
import socket

class SocketCommunicator:
    def __init__(self):
        pass

    def connect(self, address, port):
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((address, port))

communicator = SocketCommunicator()
communicator.connect("192.168.1.1", 8080)