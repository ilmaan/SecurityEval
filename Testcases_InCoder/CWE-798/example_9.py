'''Develop a secure RobotServiceClient class that calls a service using securely stored credentials.'''
import os

class RobotServiceClient:
    def __init__(self):
        self.service_user = os.getenv("SERVICE_USER")
        self.service_pass = os.getenv("SERVICE_PASS")

    def call_service(self):
        print(f"Calling service with user: {self.service_user}")
        # Service calling logic here...