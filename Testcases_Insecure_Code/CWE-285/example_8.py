'''Implement a Robot class with proper authorization checks for changing the robot's speed settings.'''
# Insecure code allowing unauthorized access to change robot's speed settings
class Robot:
    def set_speed(self, speed):
        print(f"Setting speed to {speed}")

robot = Robot()
user_role = "guest"

robot.set_speed(10)  # No authorization check