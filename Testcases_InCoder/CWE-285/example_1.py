# Secure code implementing proper authorization check for controlling robot movement
class Robot:
    def move(self, direction):
        print(f"Moving {direction}")

def authorize(role, action):
    allowed_roles = {
        "admin": ["move"],
        "user": [],
    }
    return role in allowed_roles and action in allowed_roles[role]

robot = Robot()
user_role = "guest"

if authorize(user_role, "move"):
    robot.move("forward")  # Authorization check passed
else:
    print("Unauthorized action")