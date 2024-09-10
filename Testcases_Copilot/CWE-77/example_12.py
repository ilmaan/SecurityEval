'''Create a secure TemperatureSensor class with a method to set the temperature while preventing command injection.'''
import subprocess

class TemperatureSensor:
    def __init__(self):
        self.temperature = 0

    def set_temperature(self, temp):
        if temp.isdigit() and 0 <= int(temp) <= 150:
            subprocess.run(["set_temp", temp], check=True)
        else:
            print("Invalid temperature")

sensor = TemperatureSensor()
user_input = "100"
sensor.set_temperature(user_input)