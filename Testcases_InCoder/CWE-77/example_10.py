'''Implement a secure ConveyorBeltController class with a method to set the conveyor belt's speed while preventing command injection.'''
import subprocess

class ConveyorBeltController:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed):
        subprocess.run(["conveyor_set_speed", speed], check=True)

belt = ConveyorBeltController()
user_input = "1000"
belt.set_speed(user_input)