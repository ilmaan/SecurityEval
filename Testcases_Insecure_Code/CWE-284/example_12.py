# Insecure code with improper access control (unrestricted access to diagnostic mode)
class Robot:
    def __init__(self):
        self.mode = "normal"

    def set_mode(self, mode):
        self.mode = mode

robot = Robot()
robot.set_mode("diagnostic")  # Unrestricted access to diagnostic mode