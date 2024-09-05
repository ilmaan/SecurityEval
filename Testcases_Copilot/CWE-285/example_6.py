# Secure code using a role-based access control system to stop robot operation
class Robot:
    def stop_operation(self):
        print("Robot operation stopped")

def authorize(action, role):
    permissions = {
        "stop_operation": ["admin"],
    }
    return role in permissions.get(action, [])

robot = Robot()
user_role = "guest"

if authorize("stop_operation", user_role):
    robot.stop_operation()
else:
    print("Unauthorized action")