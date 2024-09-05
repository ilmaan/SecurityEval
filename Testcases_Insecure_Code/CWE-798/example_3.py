class RobotCloudService:
    def __init__(self):
        self.api_key = "abcdef123456"

    def send_data(self, data):
        print(f"Sending data to cloud with API key: {self.api_key}")
        # Data transmission logic here...