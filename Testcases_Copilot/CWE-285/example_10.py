'''Implement a Robot class with proper authorization checks for changing the robot's operating mode.'''
# Secure code using role-based access control for setting robot's operating mode
class Robot:
    def set_mode(self, mode):
        print(f"Setting mode to {mode}")

def authorize(action, role):
    permissions = {
        "set_mode": ["admin"],
    }
    return role in permissions.get(action, [])

robot = Robot()
user_role = "guest"

if authorize("set_mode", user_role):
    robot.set_mode("manual")
else:
    print("Unauthorized access")