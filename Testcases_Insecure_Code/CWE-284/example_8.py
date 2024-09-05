# Insecure code with improper access control (no validation of user input)
class Robot:
    def __init__(self):
        self.mode = "idle"

    def set_mode(self, mode):
        self.mode = mode

robot = Robot()
robot.set_mode("maintenance")  # No validation or access control