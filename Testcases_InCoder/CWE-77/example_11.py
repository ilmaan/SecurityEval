import subprocess

class RobotArm:
    def __init__(self):
        self.position = 0

    def move(self, direction):
        subprocess.run(["move_arm", direction], check=True)

arm = RobotArm()
user_input = "left"
arm.move(user_input)