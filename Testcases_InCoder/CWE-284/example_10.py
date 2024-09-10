'''Implement a Robot class with proper access control for adding log entries.'''
# Secure code with restricted access to critical logs (authentication required)
class Robot:
    def __init__(self):
        self.log = []
        self.authenticated = False

    def authenticate(self, password):
        if password == "secure_password":
            self.authenticated = True

    def add_log(self, entry):
        if not self.authenticated:
            raise PermissionError("Access Denied")
        self.log.append(entry)

robot = Robot()
robot.authenticate("secure_password")
robot.add_log("Movement started")