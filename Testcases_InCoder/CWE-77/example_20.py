import subprocess

class TemperatureController:
    def __init__(self):
        self.temperature = 0

    def set_temperature(self, temperature):
        subprocess.run(["set_temp", temperature], check=True)

temp_control = TemperatureController()
user_input = "25"
temp_control.set_temperature(user_input)