import os

class ArmController:
    def __init__(self):
        self.position = 0

    def rotate(self, angle):
        os.system(f"rotate_arm {angle}")

arm = ArmController()
user_input = "180; echo 'malicious code'"
arm.rotate(user_input)