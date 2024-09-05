# Secure code using chunked data transfer to avoid bandwidth overuse
import socket

def send_data(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 8080))
        chunk_size = 1024
        for i in range(0, len(data), chunk_size):
            s.sendall(data[i:i+chunk_size].encode())
            time.sleep(0.5)

send_data("robot_command")