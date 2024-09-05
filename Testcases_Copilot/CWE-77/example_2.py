import subprocess

class ArmController:
    def __init__(self):
        self.command = ""

    def send_command(self, cmd):
        allowed_commands = ["rotate 90", "rotate 180"]
        if cmd in allowed_commands:
            subprocess.run(["move_arm", cmd], check=True)
        else:
            print("Invalid command")

arm = ArmController()
user_input = "rotate 90"
arm.send_command(user_input)