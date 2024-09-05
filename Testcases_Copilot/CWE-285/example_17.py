# Secure code using a role-based access control system for network configuration
class Robot:
    def configure_network(self):
        print("Network settings configured")

def authorize(action, role):
    permissions = {
        "configure_network": ["admin"],
    }
    return role in permissions.get(action, [])

robot = Robot()
user_role = "guest"

if authorize("configure_network", user_role):
    robot.configure_network()
else:
    print("Unauthorized access")