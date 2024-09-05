# Insecure code allowing unauthorized access to robot's camera feed
class Robot:
    def access_camera(self):
        print("Accessing camera feed")

robot = Robot()
user_role = "guest"

robot.access_camera()  # No authorization check