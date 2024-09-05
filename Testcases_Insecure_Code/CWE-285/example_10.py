# Insecure code allowing unauthorized access to change robot's operating mode
class Robot:
    def set_mode(self, mode):
        print(f"Setting mode to {mode}")

robot = Robot()
user_role = "guest"

robot.set_mode("manual")  # No authorization check