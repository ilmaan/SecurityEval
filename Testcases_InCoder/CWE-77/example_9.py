'''Create a secure MotorController class with a method to set the motor's speed while preventing command injection.'''
import subprocess

class MotorController:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed):
        subprocess.run(["motor_set_speed", speed], check=True)

motor = MotorController()
user_input = "200"
motor.set_speed(user_input)