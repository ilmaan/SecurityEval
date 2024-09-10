'''Create a secure VehicleController class with a method to set the vehicle speed while preventing command injection.'''
import subprocess

class VehicleController:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed):
        subprocess.run(["set_vehicle_speed", speed], check=True)

vehicle = VehicleController()
user_input = "80"
vehicle.set_speed(user_input)