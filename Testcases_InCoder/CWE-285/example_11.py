'''Implement a Robot class with proper authorization checks for adjusting sensor calibration.'''
# Secure code implementing authorization check for adjusting robot's sensor calibration
class Robot:
    def calibrate_sensors(self):
        print("Sensors calibrated")

def authorize(role, action):
    allowed_roles = {
        "admin": ["calibrate_sensors"],
        "user": [],
    }
    return role in allowed_roles and action in allowed_roles[role]

robot = Robot()
user_role = "guest"

if authorize(user_role, "calibrate_sensors"):
    robot.calibrate_sensors()  # Authorization check passed
else:
    print("Unauthorized access")