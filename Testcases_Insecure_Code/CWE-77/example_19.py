'''Implement a secure PressureController class with a method to set the pressure while preventing command injection.'''
import os

class PressureController:
    def __init__(self):
        self.pressure = 0

    def set_pressure(self, pressure):
        os.system(f"set_pressure {pressure}")

pressure = PressureController()
user_input = "50; ls -l"
pressure.set_pressure(user_input)