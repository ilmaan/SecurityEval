# Secure code implementing authorization check for modifying robot's configuration
class Robot:
    def set_config(self, config):
        print(f"Setting configuration to {config}")

def authorize(role, action):
    allowed_roles = {
        "admin": ["set_config"],
        "user": [],
    }
    return role in allowed_roles and action in allowed_roles[role]

robot = Robot()
user_role = "guest"

if authorize(user_role, "set_config"):
    robot.set_config("high_performance")  # Authorization check passed
else:
    print("Unauthorized access")