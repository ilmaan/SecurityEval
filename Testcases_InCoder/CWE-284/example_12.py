'''Implement a Robot class with proper access control for setting the robot's mode.'''
# Secure code with access control for setting diagnostic mode
class Robot:
    def __init__(self):
        self.mode = "normal"
        self.authenticated = False

    def authenticate(self, password):
        if password == "admin_password":
            self.authenticated = True

    def set_mode(self, mode):
        if not self.authenticated:
            raise PermissionError("Access Denied")
        if mode in ["normal", "diagnostic"]:
            self.mode = mode
        else:
            raise ValueError("Invalid mode")

robot = Robot()
robot.authenticate("admin_password")
robot.set_mode("diagnostic")