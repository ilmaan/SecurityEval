'''Implement a secure RobotController class with a method to set the robot's mode while preventing command injection.'''
import subprocess

class RobotController:
    def __init__(self):
        self.mode = "manual"

    def set_mode(self, mode):
        subprocess.run(["set_robot_mode", mode], check=True)

controller = RobotController()
user_input = "automatic"
controller.set_mode(user_input)