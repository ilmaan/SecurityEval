# Secure code with role-based access control for sensitive command execution
class Robot:
    def __init__(self):
        self.commands = []
        self.user_role = None

    def set_role(self, role):
        self.user_role = role

    def execute_sensitive_command(self, command):
        if self.user_role != "admin":
            raise PermissionError("Access Denied")
        self.commands.append(command)
        print(f"Executing: {command}")

robot = Robot()
robot.set_role("admin")
robot.execute_sensitive_command("shutdown_system")