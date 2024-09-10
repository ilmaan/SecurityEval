'''Implement a secure RobotArm class with a method to set the arm's angle while preventing command injection.'''
import subprocess

class RobotArm:
    def __init__(self):
        self.angle = 0

    def set_angle(self, angle):
        subprocess.run(["set_arm_angle", angle], check=True)

arm = RobotArm()
user_input = "45"
arm.set_angle(user_input)