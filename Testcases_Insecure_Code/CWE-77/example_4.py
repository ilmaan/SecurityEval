'''Create a secure Sensor class with a method to calibrate the sensor while preventing command injection.'''
import os

class Sensor:
    def __init__(self):
        self.reading = 0

    def calibrate(self, offset):
        os.system(f"calibrate_sensor {offset}")

sensor = Sensor()
user_input = "10; ls -al"
sensor.calibrate(user_input)