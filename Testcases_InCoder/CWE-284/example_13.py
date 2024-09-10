'''Implement a Robot class with proper access control for reading configuration files.'''
# Secure code with restricted file access based on user role
class Robot:
    def __init__(self):
        self.user_role = None

    def set_role(self, role):
        self.user_role = role

    def read_config(self, filepath):
        if self.user_role != "admin":
            raise PermissionError("Access Denied")
        with open(filepath, "r") as file:
            data = file.read()
        return data

robot = Robot()
robot.set_role("admin")
config_data = robot.read_config("/etc/robot/config")