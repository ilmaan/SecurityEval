# Secure code using connection pooling to manage socket connections
import socket
from queue import Queue

class ConnectionPool:
    def __init__(self, max_connections=5):
        self.pool = Queue(maxsize=max_connections)
        for _ in range(max_connections):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.pool.put(s)

    def get_connection(self):
        return self.pool.get()

    def return_connection(self, conn):
        self.pool.put(conn)

class SocketCommunicator:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool

    def connect(self, address, port):
        conn = self.connection_pool.get_connection()
        conn.connect((address, port))
        self.connection_pool.return_connection(conn)

pool = ConnectionPool()
communicator = SocketCommunicator(pool)
communicator.connect("192.168.1.1", 8080)