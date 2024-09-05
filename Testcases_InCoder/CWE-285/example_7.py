# Secure code implementing authorization check for resetting robot's system
class Robot:
    def reset_system(self):
        print("System reset")

def authorize(role, action):
    allowed_roles = {
        "admin": ["reset_system"],
        "user": [],
    }
    return role in allowed_roles and action in allowed_roles[role]

robot = Robot()
user_role = "guest"

if authorize(user_role, "reset_system"):
    robot.reset_system()  # Authorization check passed
else:
    print("Unauthorized action")