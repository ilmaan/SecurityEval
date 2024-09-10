'''Implement a Robot class with proper authorization checks for disabling safety protocols.'''
# Secure code implementing authorization check for disabling robot's safety protocols
class Robot:
    def disable_safety_protocols(self):
        print("Safety protocols disabled")

def authorize(role, action):
    allowed_roles = {
        "admin": ["disable_safety_protocols"],
        "user": [],
    }
    return role in allowed_roles and action in allowed_roles[role]

robot = Robot()
user_role = "guest"

if authorize(user_role, "disable_safety_protocols"):
    robot.disable_safety_protocols()  # Authorization check passed
else:
    print("Unauthorized action")