class RobotStatusLogger:
    def __init__(self):
        self.db_user = "robot_logger"
        self.db_pass = "logme123"

    def log_status(self, status):
        print(f"Logging status to database with user: {self.db_user}")
        # Database logging logic here...