# Secure code with controlled socket connections (using context manager)
import socket

class SocketCommunicator:
    def __init__(self):
        pass

    def connect(self, address, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((address, port))

communicator = SocketCommunicator()
communicator.connect("192.168.1.1", 8080)