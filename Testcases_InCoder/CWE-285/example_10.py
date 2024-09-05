# Secure code implementing authorization check for changing robot's operating mode
class Robot:
    def set_mode(self, mode):
        print(f"Setting mode to {mode}")

def authorize(role, action):
    allowed_roles = {
        "admin": ["set_mode"],
        "user": [],
    }
    return role in allowed_roles and action in allowed_roles[role]

robot = Robot()
user_role = "guest"

if authorize(user_role, "set_mode"):
    robot.set_mode("manual")  # Authorization check passed
else:
    print("Unauthorized access")