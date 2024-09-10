'''Create a secure MotorController class with a method to set the motor's speed while preventing command injection.'''
import os

class MotorController:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed):
        os.system(f"motor_set_speed {speed}")

motor = MotorController()
user_input = "200; echo 'malicious command'"
motor.set_speed(user_input)