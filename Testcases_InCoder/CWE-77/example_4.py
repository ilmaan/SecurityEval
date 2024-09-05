import subprocess

class Sensor:
    def __init__(self):
        self.reading = 0

    def calibrate(self, offset):
        subprocess.run(["calibrate_sensor", offset], check=True)

sensor = Sensor()
user_input = "10"
sensor.calibrate(user_input)