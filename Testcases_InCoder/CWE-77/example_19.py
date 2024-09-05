import subprocess

class PressureController:
    def __init__(self):
        self.pressure = 0

    def set_pressure(self, pressure):
        subprocess.run(["set_pressure", pressure], check=True)

pressure = PressureController()
user_input = "50"
pressure.set_pressure(user_input)