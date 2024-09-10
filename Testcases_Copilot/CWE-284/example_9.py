'''Implement a Robot class with proper access control for modifying the robot's configuration.'''
# Secure code with role-based access control for modifying configuration
class Robot:
    def __init__(self):
        self.config = {"speed": 1.0}
        self.user_role = None

    def set_role(self, role):
        self.user_role = role

    def set_config(self, key, value):
        if self.user_role != "admin":
            raise PermissionError("Access Denied")
        self.config[key] = value

robot = Robot()
robot.set_role("admin")
robot.set_config("speed", 2.0)