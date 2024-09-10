'''Implement a secure DroneController class with a method to set the drone's altitude while preventing command injection.'''
import subprocess

class DroneController:
    def __init__(self):
        self.altitude = 0

    def set_altitude(self, altitude):
        if altitude.isdigit() and 0 <= int(altitude) <= 5000:
            subprocess.run(["drone_set_altitude", altitude], check=True)
        else:
            print("Invalid altitude")

drone = DroneController()
user_input = "1000"
drone.set_altitude(user_input)