class RobotAdmin:
    def __init__(self):
        self.admin_user = "admin"
        self.admin_pass = "admin123"

    def perform_admin_task(self):
        print(f"Performing admin task with user: {self.admin_user}")
        # Admin task logic here...