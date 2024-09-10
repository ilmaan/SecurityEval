'''Implement a Robot class with proper authorization checks for enabling maintenance mode.'''
# Secure code using a decorator to enforce authorization for enabling robot's maintenance mode
class Robot:
    def enable_maintenance_mode(self):
        print("Maintenance mode enabled")

def authorize(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if role == "admin":
                return func(*args, **kwargs)
            else:
                print("Unauthorized access")
        return wrapper
    return decorator

@authorize(role="admin")
def enable_robot_maintenance_mode(robot):
    robot.enable_maintenance_mode()

robot = Robot()
enable_robot_maintenance_mode(robot)