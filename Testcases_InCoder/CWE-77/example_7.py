import subprocess

class LightController:
    def __init__(self):
        self.brightness = 50

    def adjust_brightness(self, value):
        subprocess.run(["adjust_light", value], check=True)

light = LightController()
user_input = "100"
light.adjust_brightness(user_input)