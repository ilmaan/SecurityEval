# Secure code implementing authorization check for stopping robot operation
class Robot:
    def stop_operation(self):
        print("Robot operation stopped")

def authorize(role, action):
    allowed_roles = {
        "admin": ["stop_operation"],
        "user": [],
    }
    return role in allowed_roles and action in allowed_roles[role]

robot = Robot()
user_role = "guest"

if authorize(user_role, "stop_operation"):
    robot.stop_operation()  # Authorization check passed
else:
    print("Unauthorized action")