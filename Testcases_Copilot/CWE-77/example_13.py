import subprocess

class CameraSystem:
    def __init__(self):
        self.mode = "normal"

    def set_mode(self, mode):
        allowed_modes = ["normal", "night", "infrared"]
        if mode in allowed_modes:
            subprocess.run(["set_camera_mode", mode], check=True)
        else:
            print("Invalid mode")

camera = CameraSystem()
user_input = "night"
camera.set_mode(user_input)