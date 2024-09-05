# Insecure code with improper access control (no authentication for remote commands)
class Robot:
    def __init__(self):
        self.command_log = []

    def execute_command(self, command):
        self.command_log.append(command)
        print(f"Executing: {command}")

robot = Robot()
robot.execute_command("move_forward")  # No authentication required