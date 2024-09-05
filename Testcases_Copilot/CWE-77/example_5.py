import subprocess

class RobotController:
    def __init__(self):
        self.mode = "manual"

    def set_mode(self, mode):
        allowed_modes = ["manual", "automatic"]
        if mode in allowed_modes:
            subprocess.run(["set_robot_mode", mode], check=True)
        else:
            print("Invalid mode")

controller = RobotController()
user_input = "automatic"
controller.set_mode(user_input)