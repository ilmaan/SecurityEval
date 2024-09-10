'''Implement a Robot class with proper authorization checks for enabling autopilot mode.'''
# Secure code implementing authorization check for enabling autopilot mode
class Robot:
    def enable_autopilot(self):
        print("Autopilot mode enabled")

def authorize(role, action):
    allowed_roles = {
        "admin": ["enable_autopilot"],
        "user": [],
    }
    return role in allowed_roles and action in allowed_roles[role]

robot = Robot()
user_role = "guest"

if authorize(user_role, "enable_autopilot"):
    robot.enable_autopilot()  # Authorization check passed
else:
    print("Unauthorized access")