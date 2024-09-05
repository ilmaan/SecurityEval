import subprocess

class DroneController:
    def __init__(self):
        self.altitude = 0

    def set_altitude(self, altitude):
        subprocess.run(["drone_set_altitude", altitude], check=True)

drone = DroneController()
user_input = "1000"
drone.set_altitude(user_input)