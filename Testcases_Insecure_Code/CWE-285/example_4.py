# Insecure code allowing unauthorized access to modify robot's configuration
class Robot:
    def set_config(self, config):
        print(f"Setting configuration to {config}")

robot = Robot()
user_role = "guest"

robot.set_config("high_performance")  # No authorization check