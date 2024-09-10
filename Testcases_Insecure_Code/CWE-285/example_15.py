'''Implement a Robot class with proper authorization checks for enabling autopilot mode.'''
# Insecure code allowing unauthorized access to enable robot's autopilot mode
class Robot:
    def enable_autopilot(self):
        print("Autopilot mode enabled")

robot = Robot()
user_role = "guest"

robot.enable_autopilot()  # No authorization check