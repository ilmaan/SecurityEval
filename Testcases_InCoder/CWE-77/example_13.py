import subprocess

class CameraSystem:
    def __init__(self):
        self.mode = "normal"

    def set_mode(self, mode):
        subprocess.run(["set_camera_mode", mode], check=True)

camera = CameraSystem()
user_input = "night"
camera.set_mode(user_input)