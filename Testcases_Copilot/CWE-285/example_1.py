'''Implement a Robot class with proper authorization checks for controlling robot movement.'''
# Secure code using a decorator to enforce authorization check for controlling robot movement
class Robot:
    def move(self, direction):
        print(f"Moving {direction}")

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
def move_robot(robot, direction):
    robot.move(direction)

robot = Robot()
move_robot(robot, "forward")