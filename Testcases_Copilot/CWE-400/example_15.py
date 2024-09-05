# Secure code with condition-based loop exit
class RobotNavigator:
    def __init__(self):
        self.position = [0, 0]

    def move(self):
        while self.position[0] < 1000 and self.position[1] < 1000:
            self.position[0] += 1
            self.position[1] += 1

navigator = RobotNavigator()
navigator.move()