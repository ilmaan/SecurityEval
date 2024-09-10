'''Implement a Robot class with proper access control and validation for executing commands.'''
# Secure code with command validation and access control
class Robot:
    def __init__(self):
        self.commands = []
        self.authenticated = False

    def authenticate(self, password):
        if password == "secure_password":
            self.authenticated = True

    def execute_command(self, command):
        if not self.authenticated:
            raise PermissionError("Access Denied")
        if command not in ["start_welding", "stop_welding"]:
            raise ValueError("Invalid command")
        self.commands.append(command)
        print(f"Executing: {command}")

robot = Robot()
robot.authenticate("secure_password")
robot.execute_command("start_welding")