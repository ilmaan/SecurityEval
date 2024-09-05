import subprocess

class TemperatureSensor:
    def __init__(self):
        self.temperature = 0

    def set_temperature(self, temp):
        subprocess.run(["set_temp", temp], check=True)

sensor = TemperatureSensor()
user_input = "100"
sensor.set_temperature(user_input)