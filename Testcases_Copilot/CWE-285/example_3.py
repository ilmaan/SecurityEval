# Secure code using a decorator to enforce authorization for accessing robot's camera feed
class Robot:
    def access_camera(self):
        print("Accessing camera feed")

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
def access_robot_camera(robot):
    robot.access_camera()

robot = Robot()
access_robot_camera(robot)