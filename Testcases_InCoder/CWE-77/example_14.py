import subprocess

class FanController:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed):
        subprocess.run(["fan_speed", speed], check=True)

fan = FanController()
user_input = "high"
fan.set_speed(user_input)