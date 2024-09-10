'''Implement a secure LightSystem class with a method to set the light state while preventing command injection.'''
import os

class LightSystem:
    def __init__(self):
        self.state = "off"

    def set_state(self, state):
        os.system(f"set_light {state}")

light = LightSystem()
user_input = "on; touch /tmp/malicious"
light.set_state(user_input)