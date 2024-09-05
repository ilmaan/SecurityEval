# Secure code with role-based access control for setting diagnostic mode
class Robot:
    def __init__(self):
        self.mode = "normal"
        self.user_role = None

    def set_role(self, role):
        self.user_role = role

    def set_mode(self, mode):
        if self.user_role != "admin":
            raise PermissionError("Access Denied")
        if mode in ["normal", "diagnostic"]:
            self.mode = mode
        else:
            raise ValueError("Invalid mode")

robot = Robot()
robot.set_role("admin")
robot.set_mode("diagnostic")