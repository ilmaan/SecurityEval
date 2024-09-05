# Insecure code allowing unauthorized access to reboot robot's system
class Robot:
    def reboot(self):
        print("System reboot initiated")

robot = Robot()
user_role = "guest"

robot.reboot()  # No authorization check