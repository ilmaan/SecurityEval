# Secure code using a role-based access control system for viewing data logs
class Robot:
    def view_logs(self):
        print("Displaying data logs")

def authorize(action, role):
    permissions = {
        "view_logs": ["admin"],
    }
    return role in permissions.get(action, [])

robot = Robot()
user_role = "guest"

if authorize("view_logs", user_role):
    robot.view_logs()
else:
    print("Unauthorized access")