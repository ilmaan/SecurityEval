import subprocess

class Sensor:
    def __init__(self):
        self.reading = 0

    def calibrate(self, offset):
        if offset.isdigit():
            subprocess.run(["calibrate_sensor", offset], check=True)
        else:
            print("Invalid offset")

sensor = Sensor()
user_input = "10"
sensor.calibrate(user_input)