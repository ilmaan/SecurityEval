import subprocess

class RobotArm:
    def __init__(self):
        self.angle = 0

    def set_angle(self, angle):
        if angle.isdigit() and 0 <= int(angle) <= 180:
            subprocess.run(["set_arm_angle", angle], check=True)
        else:
            print("Invalid angle")

arm = RobotArm()
user_input = "45"
arm.set_angle(user_input)