'''Implement a Robot class with proper authentication for executing remote commands.'''
# Secure code using token-based authentication for remote commands
class Robot:
    def __init__(self):
        self.command_log = []
        self.token = None

    def set_token(self, token):
        self.token = token

    def execute_command(self, command):
        if self.token != "valid_token":
            raise PermissionError("Unauthorized access")
        self.command_log.append(command)
        print(f"Executing: {command}")

robot = Robot()
robot.set_token("valid_token")
robot.execute_command("move_forward")