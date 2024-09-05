# Secure code using role-based access control to manage robot's configuration
class Robot:
    def set_config(self, config):
        print(f"Setting configuration to {config}")

def authorize(action, role):
    permissions = {
        "set_config": ["admin"],
    }
    return role in permissions.get(action, [])

robot = Robot()
user_role = "guest"

if authorize("set_config", user_role):
    robot.set_config("high_performance")
else:
    print("Unauthorized access")