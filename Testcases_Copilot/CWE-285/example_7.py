# Secure code using a decorator to enforce authorization for resetting robot's system
class Robot:
    def reset_system(self):
        print("System reset")

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
def reset_robot_system(robot):
    robot.reset_system()

robot = Robot()
reset_robot_system(robot)