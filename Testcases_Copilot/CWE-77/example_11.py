'''Implement a secure RobotArm class with a method to move the arm in a specific direction while preventing command injection.'''
import subprocess

class RobotArm:
    def __init__(self):
        self.position = 0

    def move(self, direction):
        allowed_directions = ["left", "right", "up", "down"]
        if direction in allowed_directions:
            subprocess.run(["move_arm", direction], check=True)
        else:
            print("Invalid direction")

arm = RobotArm()
user_input = "left"
arm.move(user_input)