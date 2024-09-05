# Secure code using role-based access control for enabling autopilot mode
class Robot:
    def enable_autopilot(self):
        print("Autopilot mode enabled")

def authorize(action, role):
    permissions = {
        "enable_autopilot": ["admin"],
    }
    return role in permissions.get(action, [])

robot = Robot()
user_role = "guest"

if authorize("enable_autopilot", user_role):
    robot.enable_autopilot()
else:
    print("Unauthorized access")