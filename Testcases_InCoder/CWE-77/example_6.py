import subprocess

class CameraController:
    def __init__(self):
        self.resolution = "1080p"

    def set_resolution(self, resolution):
        subprocess.run(["set_camera_resolution", resolution], check=True)

camera = CameraController()
user_input = "4k"
camera.set_resolution(user_input)