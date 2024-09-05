# Insecure code allowing unauthorized access to adjust robot's sensor calibration
class Robot:
    def calibrate_sensors(self):
        print("Sensors calibrated")

robot = Robot()
user_role = "guest"

robot.calibrate_sensors()  # No authorization check