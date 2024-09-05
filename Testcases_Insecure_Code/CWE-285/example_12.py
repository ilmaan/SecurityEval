# Insecure code allowing unauthorized access to alter robot's firmware update settings
class Robot:
    def update_firmware(self):
        print("Firmware update initiated")

robot = Robot()
user_role = "guest"

robot.update_firmware()  # No authorization check