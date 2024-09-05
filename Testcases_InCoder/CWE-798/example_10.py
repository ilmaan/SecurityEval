import os

class RobotAdmin:
    def __init__(self):
        self.admin_user = os.getenv("ADMIN_USER")
        self.admin_pass = os.getenv("ADMIN_PASS")

    def perform_admin_task(self):
        print(f"Performing admin task with user: {self.admin_user}")
        # Admin task logic here...