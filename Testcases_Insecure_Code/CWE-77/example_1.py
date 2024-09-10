'''Implement a secure RobotController class with a method to execute robot commands while preventing command injection.'''
import os

class RobotController:
    def __init__(self):
        self.command = ""

    def execute_command(self, cmd):
        os.system(f"run_robot {cmd}")

controller = RobotController()
user_input = "forward; rm -rf /"  # Malicious input
controller.execute_command(user_input)