# Secure code using a decorator to enforce authorization for initiating emergency stop
class Robot:
    def emergency_stop(self):
        print("Emergency stop initiated")

def authorize(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if role == "admin":
                return func(*args, **kwargs)
            else:
                print("Unauthorized action")
        return wrapper
    return decorator

@authorize(role="admin")
def initiate_robot_emergency_stop(robot):
    robot.emergency_stop()

robot = Robot()
initiate_robot_emergency_stop(robot)