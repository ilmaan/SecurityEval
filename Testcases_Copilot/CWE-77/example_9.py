'''Create a secure MotorController class with a method to set the motor's speed while preventing command injection.'''
import subprocess

class MotorController:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed):
        if speed.isdigit() and 0 <= int(speed) <= 300:
            subprocess.run(["motor_set_speed", speed], check=True)
        else:
            print("Invalid speed")

motor = MotorController()
user_input = "200"
motor.set_speed(user_input)