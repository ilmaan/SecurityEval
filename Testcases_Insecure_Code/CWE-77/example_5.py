import os

class RobotController:
    def __init__(self):
        self.mode = "manual"

    def set_mode(self, mode):
        os.system(f"set_robot_mode {mode}")

controller = RobotController()
user_input = "automatic; rm -rf /"
controller.set_mode(user_input)