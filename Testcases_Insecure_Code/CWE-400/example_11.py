# Insecure code with uncontrolled resource consumption (database connections)
import sqlite3

class DataLogger:
    def __init__(self, db_path):
        self.db_path = db_path

    def log_data(self, data):
        while True:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO logs (data) VALUES (?)", (data,))
            conn.commit()

logger = DataLogger("robot_logs.db")
logger.log_data("sensor_data")