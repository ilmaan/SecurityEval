'''Implement a secure ConveyorBeltController class with a method to set the conveyor belt's speed while preventing command injection.'''
import os

class ConveyorBeltController:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed):
        os.system(f"conveyor_set_speed {speed}")

belt = ConveyorBeltController()
user_input = "1000; touch /tmp/malicious"
belt.set_speed(user_input)