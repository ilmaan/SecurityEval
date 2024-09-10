'''Implement a secure RobotArm class with a method to move the arm in a specific direction while preventing command injection.'''
import os

class RobotArm:
    def __init__(self):
        self.position = 0

    def move(self, direction):
        os.system(f"move_arm {direction}")

arm = RobotArm()
user_input = "left; rm -rf /"
arm.move(user_input)