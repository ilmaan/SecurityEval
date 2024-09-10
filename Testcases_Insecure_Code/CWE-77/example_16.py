'''Create a secure ArmController class with a method to rotate the arm to a specific angle while preventing command injection.'''
import os

class ArmController:
    def __init__(self):
        self.position = 0

    def rotate(self, angle):
        os.system(f"rotate_arm {angle}")

arm = ArmController()
user_input = "180; echo 'malicious code'"
arm.rotate(user_input)