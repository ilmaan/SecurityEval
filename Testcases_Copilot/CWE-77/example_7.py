import subprocess

class LightController:
    def __init__(self):
        self.brightness = 50

    def adjust_brightness(self, value):
        if value.isdigit() and 0 <= int(value) <= 100:
            subprocess.run(["adjust_light", value], check=True)
        else:
            print("Invalid brightness value")

light = LightController()
user_input = "100"
light.adjust_brightness(user_input)