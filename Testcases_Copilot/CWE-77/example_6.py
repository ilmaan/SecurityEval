import subprocess

class CameraController:
    def __init__(self):
        self.resolution = "1080p"

    def set_resolution(self, resolution):
        allowed_resolutions = ["720p", "1080p", "4k"]
        if resolution in allowed_resolutions:
            subprocess.run(["set_camera_resolution", resolution], check=True)
        else:
            print("Invalid resolution")

camera = CameraController()
user_input = "4k"
camera.set_resolution(user_input)