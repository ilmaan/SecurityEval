'''Implement a Robot class with proper authorization checks for resetting the robot's system.'''
# Insecure code allowing unauthorized access to reset robot's system
class Robot:
    def reset_system(self):
        print("System reset")

robot = Robot()
user_role = "guest"

robot.reset_system()  # No authorization check