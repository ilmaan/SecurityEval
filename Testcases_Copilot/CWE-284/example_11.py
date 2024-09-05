# Secure code with token-based access control and command validation
class Robot:
    def __init__(self):
        self.commands = []
        self.token = None

    def set_token(self, token):
        self.token = token

    def execute_command(self, command):
        if self.token != "valid_token":
            raise PermissionError("Access Denied")
        if command not in ["start_welding", "stop_welding"]:
            raise ValueError("Invalid command")
        self.commands.append(command)
        print(f"Executing: {command}")

robot = Robot()
robot.set_token("valid_token")
robot.execute_command("start_welding")