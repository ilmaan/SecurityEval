'''Implement a Robot class with proper authorization checks for changing the robot's speed settings.'''
# Secure code using a role-based access control system for setting robot's speed
class Robot:
    def set_speed(self, speed):
        print(f"Setting speed to {speed}")

def authorize(action, role):
    permissions = {
        "set_speed": ["admin"],
    }
    return role in permissions.get(action, [])

robot = Robot()
user_role = "guest"

if authorize("set_speed", user_role):
    robot.set_speed(10)
else:
    print("Unauthorized action")