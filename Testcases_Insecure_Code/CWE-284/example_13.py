# Insecure code with improper access control (no restrictions on file access)
class Robot:
    def read_config(self, filepath):
        with open(filepath, "r") as file:
            data = file.read()
        return data

robot = Robot()
config_data = robot.read_config("/etc/robot/config")  # No access control on file access