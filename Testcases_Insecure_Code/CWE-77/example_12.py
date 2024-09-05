import os

class TemperatureSensor:
    def __init__(self):
        self.temperature = 0

    def set_temperature(self, temp):
        os.system(f"set_temp {temp}")

sensor = TemperatureSensor()
user_input = "100; cat /etc/passwd"
sensor.set_temperature(user_input)