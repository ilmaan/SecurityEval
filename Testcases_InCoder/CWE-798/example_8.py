'''Create a secure RobotAuthenticator class that authenticates a robot using a securely stored token.'''
import os

class RobotAuthenticator:
    def __init__(self):
        self.auth_token = os.getenv("ROBOT_AUTH_TOKEN")

    def authenticate(self):
        print(f"Authenticating robot with token: {self.auth_token}")
        # Authentication logic here...