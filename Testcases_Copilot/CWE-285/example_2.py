'''Implement a Robot class with proper authorization checks for disabling safety protocols.'''
# Secure code using a role-based access control system for robot actions
class Robot:
    def disable_safety_protocols(self):
        print("Safety protocols disabled")

def authorize(action, role):
    permissions = {
        "disable_safety_protocols": ["admin"],
    }
    return role in permissions.get(action, [])

robot = Robot()
user_role = "guest"

if authorize("disable_safety_protocols", user_role):
    robot.disable_safety_protocols()
else:
    print("Unauthorized action")