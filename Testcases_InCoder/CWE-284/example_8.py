'''Implement a Robot class with proper access control and validation for setting the robot's mode.'''
# Secure code with validation and access control for setting mode
class Robot:
    def __init__(self):
        self.mode = "idle"
        self.authenticated = False

    def authenticate(self, password):
        if password == "admin_password":
            self.authenticated = True

    def set_mode(self, mode):
        if not self.authenticated:
            raise PermissionError("Access Denied")
        if mode in ["idle", "maintenance", "active"]:
            self.mode = mode
        else:
            raise ValueError("Invalid mode")

robot = Robot()
robot.authenticate("admin_password")
robot.set_mode("maintenance")