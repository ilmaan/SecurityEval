'''Implement a Robot class with proper authorization checks for initiating emergency stop.'''
# Insecure code allowing unauthorized access to initiate emergency stop
class Robot:
    def emergency_stop(self):
        print("Emergency stop initiated")

robot = Robot()
user_role = "guest"

robot.emergency_stop()  # No authorization check