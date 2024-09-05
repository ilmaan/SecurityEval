# Insecure code with improper access control (unrestricted access to critical functions)
class RoboticArm:
    def __init__(self):
        self.position = [0, 0]

    def move_arm(self, x, y):
        self.position = [x, y]

arm = RoboticArm()
arm.move_arm(10, 20)  # Unrestricted access to move the arm