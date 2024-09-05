# Secure code with controlled client connections (socket limit)
import socket

class RobotServer:
    def __init__(self, port=8080, max_connections=5):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('0.0.0.0', port))
        self.server.listen(max_connections)

    def handle_clients(self):
        while True:
            client_socket, addr = self.server.accept()
            client_socket.sendall(b"Connected")

robot_server = RobotServer()
robot_server.handle_clients()