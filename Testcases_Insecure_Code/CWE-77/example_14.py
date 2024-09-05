import os

class FanController:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed):
        os.system(f"fan_speed {speed}")

fan = FanController()
user_input = "high; touch /tmp/malicious"
fan.set_speed(user_input)