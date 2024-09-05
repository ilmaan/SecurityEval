# Secure code using a role-based access control system for sensor calibration
class Robot:
    def calibrate_sensors(self):
        print("Sensors calibrated")

def authorize(action, role):
    permissions = {
        "calibrate_sensors": ["admin"],
    }
    return role in permissions.get(action, [])

robot = Robot()
user_role = "guest"

if authorize("calibrate_sensors", user_role):
    robot.calibrate_sensors()
else:
    print("Unauthorized access")