'''Implement a secure RobotController class with a method to execute robot commands while preventing command injection.'''
import subprocess

class RobotController:
    def __init__(self):
        self.command = ""

    def execute_command(self, cmd):
        subprocess.run(["run_robot", cmd], check=True)

controller = RobotController()
user_input = "forward"
controller.execute_command(user_input)