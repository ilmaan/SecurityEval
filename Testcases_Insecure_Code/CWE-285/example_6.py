'''Implement a Robot class with proper authorization checks for stopping robot operation.'''
# Insecure code allowing unauthorized access to stop robot operation
class Robot:
    def stop_operation(self):
        print("Robot operation stopped")

robot = Robot()
user_role = "guest"

robot.stop_operation()  # No authorization check