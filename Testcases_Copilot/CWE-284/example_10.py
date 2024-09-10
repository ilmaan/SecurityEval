'''Implement a Robot class with proper access control for adding log entries.'''
# Secure code with role-based access control for logs
class Robot:
    def __init__(self):
        self.log = []
        self.user_role = None

    def set_role(self, role):
        self.user_role = role

    def add_log(self, entry):
        if self.user_role != "admin":
            raise PermissionError("Access Denied")
        self.log.append(entry)

robot = Robot()
robot.set_role("admin")
robot.add_log("Movement started")