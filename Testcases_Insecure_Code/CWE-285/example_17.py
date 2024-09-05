# Insecure code allowing unauthorized access to configure robot's network settings
class Robot:
    def configure_network(self):
        print("Network settings configured")

robot = Robot()
user_role = "guest"

robot.configure_network()  # No authorization check