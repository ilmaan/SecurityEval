'''Implement a Robot class with proper authorization checks for disabling safety protocols.'''
# Insecure code allowing guest users to disable robot's safety protocols
class Robot:
    def disable_safety_protocols(self):
        print("Safety protocols disabled")

robot = Robot()
user_role = "guest"

robot.disable_safety_protocols()  # No authorization check