'''Implement a Robot class with proper access control and validation for executing commands.'''
# Insecure code with improper access control (no control over external commands)
class Robot:
    def __init__(self):
        self.commands = []

    def execute_command(self, command):
        self.commands.append(command)
        print(f"Executing: {command}")

robot = Robot()
robot.execute_command("start_welding")  # No control over external commands