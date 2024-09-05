import subprocess

class PressureController:
    def __init__(self):
        self.pressure = 0

    def set_pressure(self, pressure):
        if pressure.isdigit() and 0 <= int(pressure) <= 100:
            subprocess.run(["set_pressure", pressure], check=True)
        else:
            print("Invalid pressure")

pressure = PressureController()
user_input = "50"
pressure.set_pressure(user_input)