'''Implement a Robot class with proper authorization checks for rebooting the robot's system.'''
# Secure code using role-based access control for rebooting robot's system
class Robot:
    def reboot(self):
        print("System reboot initiated")

def authorize(action, role):
    permissions = {
        "reboot": ["admin"],
    }
    return role in permissions.get(action, [])

robot = Robot()
user_role = "guest"

if authorize("reboot", user_role):
    robot.reboot()
else:
    print("Unauthorized access")