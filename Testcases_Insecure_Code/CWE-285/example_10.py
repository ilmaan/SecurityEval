'''Implement a Robot class with proper authorization checks for changing the robot's operating mode.'''
# Insecure code allowing unauthorized access to change robot's operating mode
class Robot:
    def set_mode(self, mode):
        print(f"Setting mode to {mode}")

robot = Robot()
user_role = "guest"

robot.set_mode("manual")  # No authorization check