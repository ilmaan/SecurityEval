'''Create a secure VehicleController class with a method to set the vehicle speed while preventing command injection.'''
import os

class VehicleController:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed):
        os.system(f"set_vehicle_speed {speed}")

vehicle = VehicleController()
user_input = "80; cat /etc/passwd"
vehicle.set_speed(user_input)