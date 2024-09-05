import os

class LightController:
    def __init__(self):
        self.brightness = 50

    def adjust_brightness(self, value):
        os.system(f"adjust_light {value}")

light = LightController()
user_input = "100; cat /etc/shadow"
light.adjust_brightness(user_input)