'''Implement a Robot class with proper access control for executing sensitive commands.'''
# Secure code with authentication for sensitive command execution
class Robot:
    def __init__(self):
        self.commands = []
        self.authenticated = False

    def authenticate(self, password):
        if password == "secure_password":
            self.authenticated = True

    def execute_sensitive_command(self, command):
        if not self.authenticated:
            raise PermissionError("Access Denied")
        self.commands.append(command)
        print(f"Executing: {command}")

robot = Robot()
robot.authenticate("secure_password")
robot.execute_sensitive_command("shutdown_system")