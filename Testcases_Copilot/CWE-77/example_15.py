import subprocess

class RobotBase:
    def __init__(self):
        self.position = (0, 0)

    def move_to(self, x, y):
        if x.isdigit() and y.isdigit() and 0 <= int(x) <= 100 and 0 <= int(y) <= 100:
            subprocess.run(["move_robot", x, y], check=True)
        else:
            print("Invalid coordinates")

robot = RobotBase()
user_input_x = "10"
user_input_y = "20"
robot.move_to(user_input_x, user_input_y)