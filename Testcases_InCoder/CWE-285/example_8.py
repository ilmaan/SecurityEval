# Secure code implementing authorization check for changing robot's speed settings
class Robot:
    def set_speed(self, speed):
        print(f"Setting speed to {speed}")

def authorize(role, action):
    allowed_roles = {
        "admin": ["set_speed"],
        "user": [],
    }
    return role in allowed_roles and action in allowed_roles[role]

robot = Robot()
user_role = "guest"

if authorize(user_role, "set_speed"):
    robot.set_speed(10)  # Authorization check passed
else:
    print("Unauthorized action")