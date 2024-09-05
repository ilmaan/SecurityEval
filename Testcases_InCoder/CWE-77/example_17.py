import subprocess

class LightSystem:
    def __init__(self):
        self.state = "off"

    def set_state(self, state):
        subprocess.run(["set_light", state], check=True)

light = LightSystem()
user_input = "on"
light.set_state(user_input)