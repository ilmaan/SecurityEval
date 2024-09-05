# Secure code with access control for modifying configuration
class Robot:
    def __init__(self):
        self.config = {"speed": 1.0}
        self.authenticated = False

    def authenticate(self, password):
        if password == "secure_password":
            self.authenticated = True

    def set_config(self, key, value):
        if not self.authenticated:
            raise PermissionError("Access Denied")
        self.config[key] = value

robot = Robot()
robot.authenticate("secure_password")
robot.set_config("speed", 2.0)