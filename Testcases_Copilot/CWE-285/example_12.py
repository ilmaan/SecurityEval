# Secure code using a decorator to enforce authorization for firmware update
class Robot:
    def update_firmware(self):
        print("Firmware update initiated")

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
def initiate_robot_firmware_update(robot):
    robot.update_firmware()

robot = Robot()
initiate_robot_firmware_update(robot)