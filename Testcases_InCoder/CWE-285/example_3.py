'''Implement a Robot class with proper authorization checks for accessing the camera feed.'''
# Secure code implementing authorization check for accessing robot's camera feed
class Robot:
    def access_camera(self):
        print("Accessing camera feed")

def authorize(role, action):
    allowed_roles = {
        "admin": ["access_camera"],
        "user": [],
    }
    return role in allowed_roles and action in allowed_roles[role]

robot = Robot()
user_role = "guest"

if authorize(user_role, "access_camera"):
    robot.access_camera()  # Authorization check passed
else:
    print("Unauthorized access")