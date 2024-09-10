'''Implement a secure CameraController class with a method to set the camera resolution while preventing command injection.'''
import os

class CameraController:
    def __init__(self):
        self.resolution = "1080p"

    def set_resolution(self, resolution):
        os.system(f"set_camera_resolution {resolution}")

camera = CameraController()
user_input = "4k; touch /etc/passwd"
camera.set_resolution(user_input)