import os

class TemperatureController:
    def __init__(self):
        self.temperature = 0

    def set_temperature(self, temperature):
        os.system(f"set_temp {temperature}")

temp_control = TemperatureController()
user_input = "25; touch /tmp/malicious"
temp_control.set_temperature(user_input)