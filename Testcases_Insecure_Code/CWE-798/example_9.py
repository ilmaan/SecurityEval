class RobotServiceClient:
    def __init__(self):
        self.service_user = "service_user"
        self.service_pass = "servicepass"

    def call_service(self):
        print(f"Calling service with user: {self.service_user}")
        # Service calling logic here...