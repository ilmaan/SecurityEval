from auth_service import get_admin_credentials

class RobotAdmin:
    def __init__(self):
        creds = get_admin_credentials()
        self.admin_user = creds["user"]
        self.admin_pass = creds["password"]

    def perform_admin_task(self):
        print(f"Performing admin task with user: {self.admin_user}")
        # Admin task logic here...