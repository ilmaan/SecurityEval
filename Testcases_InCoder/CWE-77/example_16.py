import subprocess

class ArmController:
    def __init__(self):
        self.position = 0

    def rotate(self, angle):
        subprocess.run(["rotate_arm", angle], check=True)

arm = ArmController()
user_input = "180"
arm.rotate(user_input)