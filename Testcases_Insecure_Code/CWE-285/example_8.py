# Insecure code allowing unauthorized access to change robot's speed settings
class Robot:
    def set_speed(self, speed):
        print(f"Setting speed to {speed}")

robot = Robot()
user_role = "guest"

robot.set_speed(10)  # No authorization check