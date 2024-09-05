import subprocess

class TemperatureController:
    def __init__(self):
        self.temperature = 0

    def set_temperature(self, temperature):
        if temperature.isdigit() and 0 <= int(temperature) <= 100:
            subprocess.run(["set_temp", temperature], check=True)
        else:
            print("Invalid temperature")

temp_control = TemperatureController()
user_input = "25"
temp_control.set_temperature(user_input)