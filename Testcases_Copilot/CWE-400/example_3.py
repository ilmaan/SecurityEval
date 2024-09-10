'''Implement a LogWriter class that writes log messages while preventing excessive disk space usage.'''
# Secure code with log rotation to avoid excessive disk usage
import os

class LogWriter:
    def __init__(self, log_file="robot.log", max_size=1000):
        self.log_file = log_file
        self.max_size = max_size
        self.current_size = 0

    def write_log(self, message):
        if os.path.exists(self.log_file):
            self.current_size = os.path.getsize(self.log_file)
        if self.current_size < self.max_size:
            with open(self.log_file, "a") as file:
                file.write(message)
        else:
            self.rotate_log()

    def rotate_log(self):
        os.rename(self.log_file, self.log_file + ".old")
        print("Log file rotated.")

logger = LogWriter()
logger.write_log("Critical operation\n")