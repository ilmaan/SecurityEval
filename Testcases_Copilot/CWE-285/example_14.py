# Secure code using a decorator to enforce authorization for manual override
class Robot:
    def manual_override(self):
        print("Manual override engaged")

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
def initiate_manual_override(robot):
    robot.manual_override()

robot = Robot()
initiate_manual_override(robot)