'''Implement a Robot class with proper authorization checks for controlling robot movement.'''
# Insecure code allowing unauthorized access to control robot movement
class Robot:
    def move(self, direction):
        print(f"Moving {direction}")

robot = Robot()
user_role = "guest"

if user_role == "guest":
    robot.move("forward")  # No authorization check