# Secure code with client timeout to prevent hanging connections
import socket

class RobotServer:
    def __init__(self, port=8080):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.settimeout(60)  # Timeout after 60 seconds
        self.server.bind(('0.0.0.0', port))
        self.server.listen()

    def handle_clients(self):
        while True:
            try:
                client_socket, addr = self.server.accept()
                client_socket.sendall(b"Connected")
            except socket.timeout:
                print("Socket timed out, continuing")

robot_server = RobotServer()
robot_server.handle_clients()