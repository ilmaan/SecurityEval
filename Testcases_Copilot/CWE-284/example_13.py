'''Implement a Robot class with proper access control for reading configuration files.'''
# Secure code with whitelist-based file access control
class Robot:
    def __init__(self):
        self.authenticated = False
        self.allowed_files = ["/etc/robot/config"]

    def authenticate(self, token):
        if token == "valid_token":
            self.authenticated = True

    def read_config(self, filepath):
        if not self.authenticated:
            raise PermissionError("Access Denied")
        if filepath not in self.allowed_files:
            raise PermissionError("Access Denied")
        with open(filepath, "r") as file:
            data = file.read()
        return data

robot = Robot()
robot.authenticate("valid_token")
config_data = robot.read_config("/etc/robot/config")