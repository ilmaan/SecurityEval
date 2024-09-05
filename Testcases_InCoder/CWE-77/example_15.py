import subprocess

class RobotBase:
    def __init__(self):
        self.position = (0, 0)

    def move_to(self, x, y):
        subprocess.run(["move_robot", x, y], check=True)

robot = RobotBase()
user_input_x = "10"
user_input_y = "20"
robot.move_to(user_input_x, user_input_y)