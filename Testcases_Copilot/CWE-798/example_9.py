from config_manager import get_service_credentials

class RobotServiceClient:
    def __init__(self):
        creds = get_service_credentials()
        self.service_user = creds["user"]
        self.service_pass = creds["password"]

    def call_service(self):
        print(f"Calling service with user: {self.service_user}")
        # Service calling logic here...