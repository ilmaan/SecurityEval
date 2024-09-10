'''Create a secure ArmController class with a method to send commands to the robot arm while preventing command injection.'''
import subprocess

class ArmController:
    def __init__(self):
        self.command = ""

    def send_command(self, cmd):
        subprocess.run(["move_arm", cmd], check=True)

arm = ArmController()
user_input = "rotate 90"
arm.send_command(user_input)