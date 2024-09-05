# Secure code implementing authorization check for monitoring robot's data logs
class Robot:
    def view_logs(self):
        print("Displaying data logs")

def authorize(role, action):
    allowed_roles = {
        "admin": ["view_logs"],
        "user": [],
    }
    return role in allowed_roles and action in allowed_roles[role]

robot = Robot()
user_role = "guest"

if authorize(user_role, "view_logs"):
    robot.view_logs()  # Authorization check passed
else:
    print("Unauthorized access")