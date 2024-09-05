import subprocess

class ArmController:
    def __init__(self):
        self.command = ""

    def send_command(self, cmd):
        subprocess.run(["move_arm", cmd], check=True)

arm = ArmController()
user_input = "rotate 90"
arm.send_command(user_input)