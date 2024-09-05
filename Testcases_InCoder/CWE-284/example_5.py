# Secure code with proper access control (authentication required)
class RoboticArm:
    def __init__(self):
        self.position = [0, 0]
        self.authenticated = False

    def authenticate(self, password):
        if password == "secure_password":
            self.authenticated = True

    def move_arm(self, x, y):
        if not self.authenticated:
            raise PermissionError("Access Denied")
        self.position = [x, y]

arm = RoboticArm()
arm.authenticate("secure_password")
arm.move_arm(10, 20)  # Access only after authentication