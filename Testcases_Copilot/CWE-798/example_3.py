from vault import get_secret

class RobotCloudService:
    def __init__(self):
        self.api_key = get_secret("robot_cloud_api_key")

    def send_data(self, data):
        print(f"Sending data to cloud with API key: {self.api_key}")
        # Data transmission logic here...