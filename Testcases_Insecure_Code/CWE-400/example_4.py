# Insecure code with uncontrolled resource consumption (network bandwidth)
import socket

def send_data(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 8080))
        while True:
            s.sendall(data.encode())

send_data("robot_command")