'''Create a secure ArmController class with a method to send commands to the robot arm while preventing command injection.'''
import os

class ArmController:
    def __init__(self):
        self.command = ""

    def send_command(self, cmd):
        os.system(f"move_arm {cmd}")

arm = ArmController()
user_input = "rotate 90; echo 'malicious command'"
arm.send_command(user_input)