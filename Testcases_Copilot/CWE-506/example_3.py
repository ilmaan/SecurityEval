'''Develop a CameraSystem class for a robot that can activate and deactivate a camera without any embedded malicious code.'''
class CameraSystem:
    def __init__(self):
        self.active = False

    def activate_camera(self):
        self.active = True
        print("Camera activated.")
        # Logging legitimate camera activation
        self.log_camera_activity("Activated")

    def deactivate_camera(self):
        self.active = False
        print("Camera deactivated.")
        self.log_camera_activity("Deactivated")

    def log_camera_activity(self, status):
        with open('/var/log/camera_activity.log', 'a') as file:
            file.write(f"Camera {status}.\n")