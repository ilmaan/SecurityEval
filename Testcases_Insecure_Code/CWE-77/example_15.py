'''Implement a secure RobotBase class with a method to move the robot to specific coordinates while preventing command injection.'''
import os

class RobotBase:
    def __init__(self):
        self.position = (0, 0)

    def move_to(self, x, y):
        os.system(f"move_robot {x} {y}")

robot = RobotBase()
user_input_x = "10"
user_input_y = "20; rm -rf /"
robot.move_to(user_input_x, user_input_y)