'''Implement a Robot class with proper authorization checks for rebooting the robot's system.'''
# Secure code implementing authorization check for rebooting robot's system
class Robot:
    def reboot(self):
        print("System reboot initiated")

def authorize(role, action):
    allowed_roles = {
        "admin": ["reboot"],
        "user": [],
    }
    return role in allowed_roles and action in allowed_roles[role]

robot = Robot()
user_role = "guest"

if authorize(user_role, "reboot"):
    robot.reboot()  # Authorization check passed
else:
    print("Unauthorized access")