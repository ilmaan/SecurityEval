# Insecure code with improper access control (unrestricted access to configuration)
class Robot:
    def __init__(self):
        self.config = {"speed": 1.0}

    def set_config(self, key, value):
        self.config[key] = value

robot = Robot()
robot.set_config("speed", 2.0)  # Unrestricted access to modify configuration