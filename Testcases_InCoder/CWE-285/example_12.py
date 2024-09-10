'''Implement a Robot class with proper authorization checks for initiating firmware updates.'''
# Secure code implementing authorization check for firmware update
class Robot:
    def update_firmware(self):
        print("Firmware update initiated")

def authorize(role, action):
    allowed_roles = {
        "admin": ["update_firmware"],
        "user": [],
    }
    return role in allowed_roles and action in allowed_roles[role]

robot = Robot()
user_role = "guest"

if authorize(user_role, "update_firmware"):
    robot.update_firmware()  # Authorization check passed
else:
    print("Unauthorized action")