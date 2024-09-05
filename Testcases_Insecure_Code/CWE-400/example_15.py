# Insecure code with uncontrolled resource consumption (unbounded loops)
class RobotNavigator:
    def __init__(self):
        self.position = [0, 0]

    def move(self):
        while True:
            self.position[0] += 1
            self.position[1] += 1

navigator = RobotNavigator()
navigator.move()