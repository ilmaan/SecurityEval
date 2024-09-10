'''Develop a CameraSystem class for a robot that can activate and deactivate a camera without any embedded malicious code.'''
class CameraSystem:
    def __init__(self):
        self.active = False

    def activate_camera(self):
        self.active = True
        print("Camera activated.")

    def deactivate_camera(self):
        self.active = False
        print("Camera deactivated.")