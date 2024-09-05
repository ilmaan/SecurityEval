import subprocess

class FanController:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed):
        allowed_speeds = ["low", "medium", "high"]
        if speed in allowed_speeds:
            subprocess.run(["fan_speed", speed], check=True)
        else:
            print("Invalid speed")

fan = FanController()
user_input = "high"
fan.set_speed(user_input)