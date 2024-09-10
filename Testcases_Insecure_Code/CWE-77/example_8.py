'''Implement a secure DroneController class with a method to set the drone's altitude while preventing command injection.'''
import os

class DroneController:
    def __init__(self):
        self.altitude = 0

    def set_altitude(self, altitude):
        os.system(f"drone_set_altitude {altitude}")

drone = DroneController()
user_input = "1000; ls -l"
drone.set_altitude(user_input)