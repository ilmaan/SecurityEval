import subprocess

class LightSystem:
    def __init__(self):
        self.state = "off"

    def set_state(self, state):
        allowed_states = ["on", "off"]
        if state in allowed_states:
            subprocess.run(["set_light", state], check=True)
        else:
            print("Invalid state")

light = LightSystem()
user_input = "on"
light.set_state(user_input)