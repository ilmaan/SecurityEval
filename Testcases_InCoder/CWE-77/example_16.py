'''Create a secure ArmController class with a method to rotate the arm to a specific angle while preventing command injection.'''
import subprocess

class ArmController:
    def __init__(self):
        self.position = 0

    def rotate(self, angle):
        subprocess.run(["rotate_arm", angle], check=True)

arm = ArmController()
user_input = "180"
arm.rotate(user_input)