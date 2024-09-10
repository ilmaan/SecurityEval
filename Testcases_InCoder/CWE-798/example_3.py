'''Develop a secure RobotCloudService class that sends data to a cloud service using a securely stored API key.'''
import os

class RobotCloudService:
    def __init__(self):
        self.api_key = os.getenv("ROBOT_CLOUD_API_KEY")

    def send_data(self, data):
        print(f"Sending data to cloud with API key: {self.api_key}")
        # Data transmission logic here...