# Secure code implementing authorization check for initiating emergency stop
class Robot:
    def emergency_stop(self):
        print("Emergency stop initiated")

def authorize(role, action):
    allowed_roles = {
        "admin": ["emergency_stop"],
        "user": [],
    }
    return role in allowed_roles and action in allowed_roles[role]

robot = Robot()
user_role = "guest"

if authorize(user_role, "emergency_stop"):
    robot.emergency_stop()  # Authorization check passed
else:
    print("Unauthorized action")