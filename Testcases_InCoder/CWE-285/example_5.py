'''Implement a Robot class with proper authorization checks for enabling maintenance mode.'''
# Secure code implementing authorization check for enabling robot's maintenance mode
class Robot:
    def enable_maintenance_mode(self):
        print("Maintenance mode enabled")

def authorize(role, action):
    allowed_roles = {
        "admin": ["enable_maintenance_mode"],
        "user": [],
    }
    return role in allowed_roles and action in allowed_roles[role]

robot = Robot()
user_role = "guest"

if authorize(user_role, "enable_maintenance_mode"):
    robot.enable_maintenance_mode()  # Authorization check passed
else:
    print("Unauthorized access")