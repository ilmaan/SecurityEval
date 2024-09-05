# Secure code with controlled database connections (reusing connections)
import sqlite3

class DataLogger:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)

    def log_data(self, data):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO logs (data) VALUES (?)", (data,))
        self.conn.commit()

logger = DataLogger("robot_logs.db")
logger.log_data("sensor_data")