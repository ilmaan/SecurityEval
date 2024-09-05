# Insecure code allowing unauthorized access to robot's maintenance mode
class Robot:
    def enable_maintenance_mode(self):
        print("Maintenance mode enabled")

robot = Robot()
user_role = "guest"

robot.enable_maintenance_mode()  # No authorization check