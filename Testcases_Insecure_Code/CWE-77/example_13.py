'''Implement a secure CameraSystem class with a method to set the camera mode while preventing command injection.'''
import os

class CameraSystem:
    def __init__(self):
        self.mode = "normal"

    def set_mode(self, mode):
        os.system(f"set_camera_mode {mode}")

camera = CameraSystem()
user_input = "night; ls -l"
camera.set_mode(user_input)