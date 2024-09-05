import subprocess

class ArmController:
    def __init__(self):
        self.position = 0

    def rotate(self, angle):
        if angle.isdigit() and 0 <= int(angle) <= 360:
            subprocess.run(["rotate_arm", angle], check=True)
        else:
            print("Invalid angle")

arm = ArmController()
user_input = "180"
arm.rotate(user_input)