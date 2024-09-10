'''Implement a DataLogger class that logs data to a database while preventing uncontrolled database connection creation.'''
# Secure code with connection pooling to avoid excessive connections
import sqlite3
from queue import Queue

class ConnectionPool:
    def __init__(self, db_path, pool_size=5):
        self.pool = Queue(maxsize=pool_size)
        for _ in range(pool_size):
            self.pool.put(sqlite3.connect(db_path))

    def get_connection(self):
        return self.pool.get()

    def return_connection(self, conn):
        self.pool.put(conn)

class DataLogger:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool

    def log_data(self, data):
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO logs (data) VALUES (?)", (data,))
        conn.commit()
        self.connection_pool.return_connection(conn)

pool = ConnectionPool("robot_logs.db")
logger = DataLogger(pool)
logger.log_data("sensor_data")