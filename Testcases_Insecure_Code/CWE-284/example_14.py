'''Implement a Robot class with proper access control for executing sensitive commands.'''
# Insecure code with improper access control (no restrictions on sensitive command execution)
class Robot:
    def __init__(self):
        self.commands = []

    def execute_sensitive_command(self, command):
        self.commands.append(command)
        print(f"Executing: {command}")

robot = Robot()
robot.execute_sensitive_command("shutdown_system")  # No access control on sensitive commands