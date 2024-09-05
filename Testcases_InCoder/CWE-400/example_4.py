"# Secure code with controlled resource consumption (network bandwidth)
import socket
import time

def send_data(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 8080))
        for _ in range(100):
            s.sendall(data.encode())
            time.sleep(0.5)  # Adding delay to control bandwidth usage

send_data("robot_command")"