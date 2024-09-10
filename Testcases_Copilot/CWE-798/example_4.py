'''Implement a secure RobotStatusLogger class that logs robot status to a database without exposing database credentials in the code.'''
class RobotStatusLogger:
    def __init__(self, config):
        self.db_user = config.db_user
        self.db_pass = config.db_pass

    def log_status(self, status):
        print(f"Logging status to database with user: {self.db_user}")
        # Database logging logic here...